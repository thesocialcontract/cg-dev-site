from wagtail import blocks
from django import forms

CODE_BLOCK_LANGUAGES = (
    ('bash', 'Bash/Shell'),
    ('css', 'CSS'),
    ('diff', 'diff'),
    ('html', 'HTML'),
    ('javascript', 'Javascript'),
    ('json', 'JSON'),
    ('python', 'Python'),
    ('scss', 'SCSS'),
    ('yaml', 'YAML'),
    ('django', 'Django/Jinja2'),
    ('haskell', 'Haskell'),
    ('ruby', 'Ruby'),
    ('sql', 'SQL'),
    ('typescript', 'TypeScript'),
    ('java', 'Java'),
    ('csharp', 'C#'),
)

class CodeBlock(blocks.StructBlock):
    language = blocks.ChoiceBlock(choices=CODE_BLOCK_LANGUAGES, default="python")
    text = blocks.TextBlock(rows=20)
    
    class Meta:
        template="cms/blocks/code_block.html"
        icon = "code"
        label = "Code Block"