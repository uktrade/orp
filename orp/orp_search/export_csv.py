from datetime import datetime

from django.conf import settings

# from core.models import Report


def export_csv_header() -> list[str]:
    """Export CSV header.

    Returns a list for the export CSV header.
    """
    return [
        "Report Id",
        "Start date",
        "End date",
        "Filing date",
        "Company",
        "Company number",
        "Payments made in the reporting period",
        "Average time to pay",
        "% Invoices paid within 30 days",
        "% Invoices paid between 31 and 60 days",
        "% Invoices paid later than 60 days",
        "% Invoices not paid within agreed terms",
        "Shortest (or only) standard payment period",
        "Longest standard payment period",
        "Maximum contractual payment period",
        "Payment terms have changed",
        "Suppliers notified of changes",
        "Participates in payment codes",
        "E-Invoicing offered",
        "Supply-chain financing offered",
        "Policy covers charges for remaining on supplier list",
        "Charges have been made for remaining on supplier list",
        "URL",
    ]


def format_date(date_value) -> str:
    """Format date.

    Returns a '%Y-%m-%d' formatted date string used in the csv.
    """
    if isinstance(date_value, datetime):
        return date_value.strftime("%Y-%m-%d")
    return str(date_value)


def report_row(report_id: int, report_data: dict, contract_data: dict) -> list:
    """Report row.

    Return a list used to write a csv row.
    """
    return [
        report_id,
        format_date(report_data["reporting_period_start_date"]),
        format_date(report_data["reporting_period_end_date"]),
        format_date(report_data["filing_date"]),
        report_data["company_name"],
        report_data["company_number"],
        report_data["qualifying_contracts_in_period"],
        contract_data.get("average_paid_days", ""),
        contract_data.get("paid_within_30_days_pct", ""),
        contract_data.get("paid_31_to_60_days_pct", ""),
        contract_data.get("paid_after_61_days_pct", ""),
        contract_data.get("paid_later_than_terms_pct", ""),
        contract_data.get("payment_shortest_period_days", ""),
        contract_data.get("payment_longest_period_days", ""),
        contract_data.get("payment_max_period_days", ""),
        contract_data.get("payment_terms_changed_comment", ""),
        contract_data.get("payment_terms_changed_notified_comment", ""),
        "true" if report_data["code_of_practice"] else "false",
        contract_data.get("other_electronic_invoicing", ""),
        contract_data.get("other_supply_chain_finance", ""),
        contract_data.get("other_retention_charges_in_policy", ""),
        contract_data.get("other_retention_charges_in_past", ""),
        f"{settings.HOSTNAME}/report/{report_id}",
    ]


# def get_all_reports_sorted() -> list[dict]:
#     """Get all reports ordered by ID.

#     Returns a list of reports in ascending order of ID."""
#     reports = Report.objects.all().order_by("id")
#     return [
#         {
#             "report_id": report.id,
#             "company_name": report.company_name,
#             "company_number": report.company_id,
#             "reporting_period_start_date": report.reporting_period_start_date,
#             "reporting_period_end_date": report.reporting_period_end_date,
#             "filing_date": report.filing_date,
#             "approved_by": report.approved_by,
#             "qualifying_contracts_in_period": report.qualifying_contracts_in_period,  # noqa
#             "code_of_practice": report.code_of_practice,
#         }
#         for report in reports
#     ]
