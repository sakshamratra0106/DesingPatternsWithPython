
def generate_webform(field_list):
    """

    :param field_list:
    :return:

    Generate Fields
    """
    generated_fields = "\n".join(
        map(
            lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x),
            field_list
            )
        )
    return "<form>{fields}</form>".format(fields=generated_fields)


def build_html_form(fields):
    """

    :param fields:
    :return:

    Take Field Forms and Create a WebPage using HTML and dave it in File "form_file.html"
    """
    with open("form_file.html", "w") as f:
        f.write(
        "<html><body>{}</body></html>".format(generate_webform(fields))
        )


if __name__ == "__main__":
    fields = ["name", "age", "email", "telephone"]
    print(build_html_form(fields))