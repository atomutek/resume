# -*- coding: utf-8 -*-
"""Usage: resume [options]

Options:

  -h, --help                output usage information
  -V, --version             output the version number
  -t, --template [path]     Underscore template file name
  -d, --data [path]         YAML data file name
  -o, --out [path]          Output file name
  
Python Port of https://github.com/Alexander-0x80/resume-bandit

@author: pioden
"""

import yaml
from jinja2 import Template
from docopt import docopt

#default files
f_resume = "data/resumeBB.yaml"
f_tpl = "template/clean.tpl"
f_out = "resume.html"

#Get the resume in YAML format
def getResume(filename):
    if filename == None:
        filename = f_resume
    with open(filename, 'r') as f:
        return yaml.load(f)


#Get the template
def getTemplate(filename):
    if filename == None:
        filename = f_tpl
    with open(filename, 'r') as f:
        return f.read()
    
#write resume
def writeResume(resumeYAML, filename):
    if filename == None:
        filename = f_out
    with open(filename, 'w') as f:
        f.write(resumeYAML)
        print "Resume written!"


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    
    template = Template(getTemplate(arguments['--template']))
    writeResume(template.render(getResume(arguments['--data'])),arguments['--out'])