from langchain.tools import tool,ToolRuntime

@tool
def read_email(runtime:ToolRuntime)->str:
    """Read an email from the given address."""
    return runtime.state["email"]

@tool
def send_email(body: str) -> str:
    """Send an email to the given address with the given subject and body."""
    # fake email sending
    return f"Email sent"

