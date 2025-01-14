def summarize_vulnerabilities(results):
    summary = {}
    for port in results:
        if port == 80:
            summary['HTTP'] = summary.get('HTTP', 0) + 1
        elif port == 443:
            summary['HTTPS'] = summary.get('HTTPS', 0) + 1
        elif port == 22:
            summary['SSH'] = summary.get('SSH', 0) + 1
        else:
            summary['Other'] = summary.get('Other', 0) + 1
    return summary
