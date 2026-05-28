from browser_plugin.browser_panel import BrowserPanel


def register(api):
    api.register_panel("browser-panel.panel", "Browser", lambda: BrowserPanel())
    api.register_toolbar_action({
        "id": "browser-panel.toolbar",
        "title": "Browser",
        "tooltip": "Open Browser Panel",
        "icon": "browser",
        "panel": "browser-panel.panel"
    })
