from staticjinja import Site


if __name__ == "__main__":
    site = Site.make_site(outpath='html')
    site.render()
