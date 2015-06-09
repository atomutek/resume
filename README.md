# Resume

Resume is a Python port of [resume-bandit](https://github.com/Alexander-0x80/resume-bandit) by [Alexander Ovchinnikov](https://github.com/Alexander-0x80). With Resume, you can generate a HTML resume from a YAML doc and a template (.tpl).

## Usage

    Usage: python resume.py [options]

    Options:
      -h, --help                help information
      -t, --template [path]     template file name
      -d, --data [path]         YAML data file name
      -o, --out [path]          output file name
      
If no command line arguments are given, resume has the defaults of : 

     $ python resume.py -t templates/clean.tpl -d data/resumeBB.yaml -o resume.html

## Example

An example of the ouput can be seen in the [Example folder](https://github.com/pioden/resume/example/).

## Dependencies

You might have to install the following libraries :

* [jinja2](http://jinja.pocoo.org/)
* [docopt](http://docopt.org/) 

## Future work

* add a Bibtex option for academia people
* add other templates
* add other output formats (pdf, etc.)

## Support

Please [open an issue](https://github.com/pioden/resume/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/pioden/resume/compare/).
