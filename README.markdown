PRO runs processes and restarts them when it observes file changes.

PRO only does two things, but it does them well: it runs processes,
and restarts select processes when their dependent files change.
PRO is designed to be useful for running processes in development, but
there are probably better options for running your processes in production.

Installation
------------

    pip install pro


Usage
-----

    pro runfile.py

Your runfile contains the description of which processes to run, and
an optional list of files to observe for each process group. A process
can be defined as a command to run as a string, or as a CMD object,
which can specify a directory in which to run.

Example runfile.py:

    import os
    from pro import CMD, run

    run(CMD('python manage.py runserver 8080', cd='example_project'))
    run('python -m SimpleHTTPServer 8888', watch_list=['watchme'])

    sass_file = 'static/css/style.sass'
    run('sass %s' % sass_file, watch_list=[sass_file])

    template_dir="static/templates"
    handlebars_inputs=os.path.join(template_dir, '*.handlebars')
    handlebars_output=os.path.join(template_dir, 'templates.js')

    cmd = 'handlebars `ls %s` -f "%s"' % (handlebars_inputs, handlebars_output)
    run(cmd, watch_list=[handlebars_inputs])





