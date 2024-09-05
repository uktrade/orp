import logging
import xml.etree.ElementTree as ElementTree  # nosec

logger = logging.getLogger(__name__)


def pingdom_status(status_str: str, response_time_value: float) -> str:
    """Pingdom status.

    Returns Pingdom compatible XML response.
    """
    root = ElementTree.Element("root")
    pingdom_http_custom_check = ElementTree.SubElement(
        root, "pingdom_http_custom_check"
    )
    status = ElementTree.SubElement(pingdom_http_custom_check, "status")
    strong = ElementTree.SubElement(status, "strong")
    strong.text = str(status_str)
    response_time = ElementTree.SubElement(
        pingdom_http_custom_check, "response_time"
    )
    strong = ElementTree.SubElement(response_time, "strong")
    strong.text = str(response_time_value)
    return ElementTree.tostring(root, encoding="unicode", method="xml")


def application_service_health() -> str:
    """Report application service health.

    Returns a pingdom compatible XML string response.
    TODO: Ping various services to get average response time and status.
    """
    return pingdom_status("OK", 1.0)
