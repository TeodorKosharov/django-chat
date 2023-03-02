def site_theme_middleware(get_response):
    def middleware(request, *args, **kwargs):
        response = get_response(request)
        print(response)
        print(request)
        print(args)
        print(kwargs)

    return middleware
