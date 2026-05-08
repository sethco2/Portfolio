"""Inject site-wide identity values so templates don't hard-code them."""


def site_meta(request):
    return {
        "SITE_OWNER": "Seth Grant",
        "SITE_TAGLINE": (
            "I enjoy exploring new opportunities of innovation "
            "by using AI and human creativity."
        ),
        "SITE_EMAIL": "sethngrant2003@gmail.com",
        "SITE_LINKEDIN": "https://www.linkedin.com/in/sethngrant/",
        "SITE_GITHUB": "https://github.com/sethco2",
        "SITE_INSTAGRAM": "https://www.instagram.com/sethngrant/",
        "SITE_TIKTOK": "https://www.tiktok.com/@seethlifts",
    }
