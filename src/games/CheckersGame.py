

from typing import Optional
import nextcord







class GameCheckersStartView(nextcord.ui.View):
    def __init__(self, *, timeout: float | None = 180, auto_defer: bool = True) -> None:
        super().__init__(timeout=timeout, auto_defer=auto_defer)
        self.category_id: int = 1093504561538412654
    





class GameCheckersView(nextcord.ui.View):
    def __init__(self, *, timeout: float | None = 180, auto_defer: bool = True):
        super().__init__(timeout=timeout, auto_defer=auto_defer)









