import csv
import json
import xml.etree.ElementTree as ET

def export_results(results, export_format):
    if export_format == 'csv':
        with open('scan_results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Port'])
            for result in results:
                writer.writerow([result])
    elif export_format == 'json':
        with open('scan_results.json', 'w') as file:
            json.dump(results, file, indent=4)
    elif export_format == 'xml':
        root = ET.Element("ScanResults")
        for result in results:
            port_element = ET.SubElement(root, "Port")
            port_element.text = str(result)
        tree = ET.ElementTree(root)
        tree.write("scan_results.xml")
