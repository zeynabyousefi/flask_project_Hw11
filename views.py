from flask import redirect, url_for, request, Response, render_template
import translators as ts


# from translators import apis


def translate(from_lang: str, target_lang: str, provider: str):
    if request.method == "GET":
        return render_template("translate_page.html")
    if request.method == "POST":
        target_lang = target_lang
        text = request.form.get("message")
        if from_lang is not None:
            if provider is None:
                provider = "google"
            else:
                provider = provider
            from_lang = from_lang
            output = ts.translate_html(text, from_language=from_lang, to_language=target_lang, host=provider)
        else:
            provider = "google"
            output = ts.translate_html(text, to_language=target_lang, host=provider)
        return render_template("result.html", output_message=output)
