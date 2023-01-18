import router


def main():
    return router.template("frontend/template.html", "My Website", "")


router.addRoute("/", main)
router.runApp(81)
