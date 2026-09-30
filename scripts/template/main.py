<%!
    import shutil
    from logging import getLogger

    import onlinejudge_template.generator.python as python
    import onlinejudge_template.generator.hook as hook
    import onlinejudge_template.generator._utils as utils
%>\
<%
    logger = getLogger(__name__)
    analyzed = utils.get_analyzed(data)
    yesno = 'YES' in analyzed.constants and 'NO' in analyzed.constants
    if not shutil.which("yapf"):
        logger.warning("yapf is not installed. If you want to generate well-formatted code, please install it. You can use $ pip3 install yapf")
    else:
        format_config = "{" + ", ".join([
            "BASED_ON_STYLE: google",
            "COLUMN_LIMIT: 9999",
        ]) + "}"
        hook.register_filter_command(["yapf", "--style", format_config], data=data)
%>\
#!/usr/bin/env python3

${python.declare_constants(data)}

% if yesno:
# def solve(${python.formal_arguments(data)}) -> bool:
% else:
# def solve(${python.formal_arguments(data)}) -> ${python.return_type(data)}:
% endif
def solve(${python.formal_arguments(data, typed=False)}):
    pass  # TODO: edit here

def main():
${python.read_input(data)}
% if yesno:
    print(YES if solve(${python.actual_arguments(data)}) else NO)
% else:
    ${python.return_value(data)} = solve(${python.actual_arguments(data)})
${python.write_output(data)}
% endif

if __name__ == '__main__':
    main()
