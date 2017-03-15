def file_name(path):
    return path.split('/')[-1]

def file_extension(file):
    return file.split('.')[-1]

file_extensions = [
    'html', 'py', 'rb', 'erb', 'java', 'swift', 'c', 'cpp', 'cs', 'sql', 'css', 'js'
]

line_comment_tokens = {
    'py': '#',
    'rb': '#',
    'java': '//',
    'swift': '//',
    'c': '//',
    'cpp': '//',
    'sql': '--',
    'js': '//'
}