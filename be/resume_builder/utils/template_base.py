prompt_header_template = """
- **Template to Use**
```
<header>
  <h1>[Name and Surname]</h1>
  <div class="contact-info"> 
      <p class="fas fa-map-marker-alt"> <span>[Your City, Your Country]</span></p> 
      <p class="fas fa-phone"> <span>[Your Prefix Phone number]</span></p> 
      <p class="fas fa-envelope"> <span>[Your Email]</span></p> 
      <p class="fab fa-linkedin"> <a href="[Link LinkedIn account]">LinkedIn</a></p> 
      <p class="fab fa-github"> <a href=[Link GitHub account]">GitHub</a></p> 
  </div>
</header>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_objective_template = """
- **Template to Use**
```
<section id="Objective">
    <h2>Objective</h2>
    <div class="objective">[description]</div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_education_template = """
- **Template to Use**
```
<section id="education">
    <h2>Education</h2>
    <div class="entry">
        <div class="en-entry">
            <div class="en-split">
                <div class="en-join">
                    <span class="entry-name">[University Name]</span>
                    <span class="entry-location">[Location]</span>
                </div>
                <span>[Start Year] – [End Year]</span>
            </div>
            <span>[Degree] in [Field of Study], [Grade]</span>
        </div>
    </div>
    <div class="entry">
        <div class="en-entry">
            <div class="en-split">
                <div class="en-join">
                    <span class="entry-name">[University Name]</span>
                    <span class="entry-location">[Location]</span>
                </div>
                <span>[Start Year] – [End Year]</span>
            </div>
            <span>[Degree] in [Field of Study], [Grade]</span>
        </div>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```"""


prompt_working_experience_template = """
- **Template to Use**
```
<section id="work-experience">
    <h2>Work Experience</h2>
    <div class="entry">
        <div class="en-entry">
            <div class="en-split">
                <span class="entry-name">[Your Job Title]</span>
                <span>[Start Date] – [End Date]</span>
            </div>
            <div class="en-split">
                <span>[Company Name]</span>
                <span class="entry-location">[Location]</span>
            </div>
            <ul class="compact-list">
                <li>[Describe your responsibilities and achievements in this role] </li>
                <li>[Describe any key projects or technologies you worked with]  </li>
                <li>[Mention any notable accomplishments or results]</li>
            </ul>
        </div>
    </div>
    <div class="entry">
        <div class="en-entry">
            <div class="en-split">
                <span class="entry-name">[Your Job Title]</span>,
                <span>[Start Date] – [End Date]</span>
            </div>
            <div class="en-split">
                <span>[Company Name]</span>
                <span class="entry-location">[Location]</span>
            </div>
            <ul class="compact-list">
                <li>[Describe your responsibilities and achievements in this role] </li>
                <li>[Describe any key projects or technologies you worked with]  </li>
                <li>[Mention any notable accomplishments or results]</li>
            </ul>
        </div>
    </div>
    <div class="entry">
        <div class="en-entry">
            <div class="en-split">
                <span class="entry-name">[Your Job Title]</span>,
                <span>[Start Date] – [End Date]</span>
            </div>
            <div class="en-split">
                <span>[Company Name]</span>
                <span class="entry-location">[Location]</span>
            </div>
            <ul class="compact-list">
                <li>[Describe your responsibilities and achievements in this role] </li>
                <li>[Describe any key projects or technologies you worked with]  </li>
                <li>[Mention any notable accomplishments or results]</li>
            </ul>
        </div>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```"""


prompt_side_projects_template = """
- **Template to Use**
```
<section id="side-projects">
    <h2>Projects</h2>
    <div class="entry">
        <div class="en-entry">
            <div class="en-join">
                <span class="entry-name">[Project Name]</span>
                <a href="[Github Repo or Link]">(visit)</a>
            </div>
            <ul class="compact-list">
              <li>[Describe any notable recognition or reception]</li>
              <li>[Describe any notable recognition or reception]</li>
              <li>[Describe any notable recognition or reception]</li>
            </ul>
        </div>
    </div>
    <div class="entry">
        <div class="en-entry">
            <div class="en-join">
                <span class="entry-name">[Project Name]</span>
                <a href="[Github Repo or Link]">(visit)</a>
            </div>
            <ul class="compact-list">
              <li>[Describe any notable recognition or reception]</li>
              <li>[Describe any notable recognition or reception]</li>
              <li>[Describe any notable recognition or reception]</li>
            </ul>
        </div>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""


prompt_achievements_template = """
- **Template to Use**
```
<section id="achievements">
  <h2>Achievements</h2>
  <div class="two-column">
      <span class="left-name">[name]</span>
      <div class="right-list">[description]</div>
  </div>
  <div class="two-column">
      <span class="left-name">[name]</span>
      <div class="right-list">[description]</div>
  </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_certifications_template = """
- **Template to Use**
```
<section id="certifications">
  <h2>Certifications</h2>
  <div class="two-column">
    <span class="left-name">[name]</span>
    <div class="right-list">[description]</div>
  </div>
  <div class="two-column">
      <span class="left-name">[name]</span>
      <div class="right-list">[description]</div>
  </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_additional_skills_template = """
- **Template to Use**
'''
<section id="skills-languages">
  <h2>Skills</h2>
  <div class="two-column">
      <span class="left-name">Technical Skills</span>
      <div class="right-list">
        [Specific Skill or Technology], [Specific Skill or Technology], [Specific Skill or Technology], [Specific Skill or Technology], [Specific Skill or Technology], [Specific Skill or Technology]
      </div>
  </div>
  <div class="two-column">
      <span class="left-name">Soft Skills</span>
      <div class="right-list">
          [Specific Soft Skill], [Specific Soft Skill], [Specific Soft Skill], [Specific Soft Skill], [Specific Soft Skill]
      </div>
  </div>
</section>
'''
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""
