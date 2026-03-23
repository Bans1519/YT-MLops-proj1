import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error information including file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()

    # Fallback if this is called outside of an active exception context
    if exc_tb is None:
        return f"Error: {str(error)}"

    trace_lines = ["\n" + "="*20 + " ERROR TRACE " + "="*20]

    # Walking through the stack frames
    while exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        trace_lines.append(f"→ File: [{file_name}] | Line: [{line_number}]")
        exc_tb = exc_tb.tb_next

    trace_lines.append("="*53)
    trace_lines.append(f"Root Cause: {str(error)}")
    trace_lines.append("="*53 + "\n")

    return "\n".join(trace_lines)

class MyException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        :param error_message: error message in string or exception object
        :param error_detail: sys module
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message