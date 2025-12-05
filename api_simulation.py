def create_incident_ticket(issue_summary, severity):
    return {
        "ticket_id": "INC-" + str(hash(issue_summary) % 10000),
        "status": "CREATED",
        "severity": severity,
        "message": f"Incident logged for: {issue_summary}",
    }
