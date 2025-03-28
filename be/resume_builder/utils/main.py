import base64
import os
from pathlib import Path
import warnings
import yaml

from resume_builder.utils.manager_facade import FacadeManager
from resume_builder.utils.resume import Resume
from resume_builder.utils.style_manager import StyleManager
from resume_builder.utils.resume_generator import ResumeGenerator

# Define custom deprecation warnings
class CustomDeprecationWarning(DeprecationWarning):
    """Custom warning for deprecated features."""
    pass

class CustomPendingDeprecationWarning(PendingDeprecationWarning):
    """Custom pending deprecation warning."""
    pass

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)

@staticmethod
def validate_secrets(secrets_yaml_path: Path):
    try:
        with open(secrets_yaml_path, 'r') as stream:
            secrets = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        raise Exception(f"Error reading secrets file {secrets_yaml_path}: {exc}")
    except FileNotFoundError:
        raise Exception(f"Secrets file not found: {secrets_yaml_path}")
    mandatory_secrets = ['openai_api_key']
    for secret in mandatory_secrets:
        if secret not in secrets:
            raise Exception(f"Missing secret in file {secrets_yaml_path}: {secret}")
    if not secrets['openai_api_key']:
        raise Exception(f"OpenAI API key cannot be empty in secrets file {secrets_yaml_path}.")
    return secrets['openai_api_key']

def printred(text):
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"{RED}{text}{RESET}")

def main():  
    folder = "log"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    log_path = Path(folder).resolve()
    secrets_yaml_path = Path(__file__).parent / "secrets.yaml"
    resume_yaml_path = Path(__file__).parent / "plain_text_resume.yaml"
    api_key = validate_secrets(secrets_yaml_path)
    
    with open(resume_yaml_path, "r") as file:
        plain_text_resume = file.read()
        resume_object = Resume(plain_text_resume)
    
    style_manager = StyleManager()
    resume_generator = ResumeGenerator()
    
    manager = FacadeManager(api_key, style_manager, resume_generator, resume_object, log_path)

    if os.path.exists("resume.pdf"):
        os.remove("resume.pdf")
    
    with open("resume.pdf", "xb") as f:
        f.write(base64.b64decode(manager.pdf_base64()))

if __name__ == "__main__":
    main()