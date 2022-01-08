from flask import Flask, render_template, request
import re


app = Flask(__name__)


def typographer(text):
    def nbsp_repl(match):
        return match[0].replace(' ', '&nbsp;')
    
    text = re.sub(r'(?<=\W)["\'](?=\S)', '&laquo;', text)     # quotas
    text = re.sub(r'(?<=\S)["\'](?=\W)', '&raquo;', text)
    text = re.sub(r'(?<=\A)["\'](?=\S)', '&laquo;', text)
    text = re.sub(r'(?<=\S)["\'](?=\Z)', '&raquo;', text)

    text = re.sub(r'(?<= )-(?= )', '&mdash;', text)     # m-dash

    text = re.sub(r'(?<=\d)-(?=\d)', '&ndash;', text)   # n-dash

    text = re.sub(r'(?<=\s)\d+ \D', nbsp_repl, text)    # num nbsp word

    text = re.sub(' +', ' ', text)                      # whitespaces
    text = re.sub('( *\r\n| *\n)+', '\n', text)         # new lines

    text = re.sub(r'(?<=\s)\D\D? \D', nbsp_repl, text)  # 1,2sym nbsp word
    return text


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def work():
    text = request.form['text']
    processed_parts = []
    for text_part in re.split(r'(<.*?>)', text):
        if len(text_part) > 0 and text_part[0] != '<':     # not html
            text_part = typographer(text_part)
        processed_parts.append(text_part)
    out_text = ''.join(processed_parts)
    return render_template('form.html', text=text, out_text=out_text)


if __name__ == "__main__":
    app.run()
