from shl.ui_tree.ui_node import UINode
from shl.ui_tree.ui_tree_builder import UITreeBuilder

class PlaywrightUITreeBuilder(UITreeBuilder):
    def __init__(self, page):
        self.page = page

    def build_tree(self):
        root = self.page.locator("body")
        return [self._build_node(root)]

    def _build_node(self, locator):
        node = UINode(
            id=locator.get_attribute("id"),
            type=locator.evaluate("el => el.tagName.toLowerCase()"),
            text=locator.inner_text(),
            selector=locator.selector
        )

        children = locator.locator(":scope > *")
        count = children.count()

        for i in range(count):
            child = children.nth(i)
            node.add_child(self._build_node(child))

        return node
