from {__project_name__} import app


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port="6767",
        debug=True,
        auto_reload=True
    )
