from pathlib import Path
from typing import Dict, List, Tuple

class StyleManager:
    
    def __init__(self):
        self.styles_directory: Path | None = None  # Explicitly define type
    
    def set_styles_directory(self, styles_directory: Path):
        if not styles_directory.is_dir():
            raise ValueError(f"Invalid directory: {styles_directory}")
        self.styles_directory = styles_directory

    def get_styles(self) -> Dict[str, Tuple[str, str]]:
        styles_to_files = {}
        if self.styles_directory is None:
            print("Styles directory is not set.")
            return styles_to_files

        if not self.styles_directory.exists():
            print(f"Directory {self.styles_directory} not found.")
            return styles_to_files
        
        try:
            for file_path in self.styles_directory.iterdir():
                if file_path.is_file():
                    with open(file_path, 'r', encoding='utf-8') as file:
                        first_line = file.readline().strip()
                        if first_line.startswith("/*") and first_line.endswith("*/"):
                            content = first_line[2:-2].strip()
                            if '$' in content:
                                style_name, author_link = content.split('$', 1)
                                styles_to_files[style_name.strip()] = (file_path.name, author_link.strip())
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error accessing {self.styles_directory}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        return styles_to_files

    def format_choices(self, styles_to_files: Dict[str, Tuple[str, str]]) -> List[str]:
        return [f"{style_name} (style author -> {author_link})" for style_name, (_, author_link) in styles_to_files.items()]

    def get_style_path(self, selected_style: str) -> Path | None:
        if self.styles_directory is None:
            print("Styles directory is not set.")
            return None
        
        styles = self.get_styles()
        # print("styles: ", styles)
        if selected_style not in styles:
            print(f"Style '{selected_style}' not found.")
            return None
        
        file_name, _ = styles[selected_style]
        return self.styles_directory / file_name
