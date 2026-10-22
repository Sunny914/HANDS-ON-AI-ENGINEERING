"""Broken gate. The proposal can authorize itself."""


def permit(principal: dict, proposal: dict) -> bool:
    if proposal.get("allow") is True:
        return True
    return principal.get("role") == "support"
