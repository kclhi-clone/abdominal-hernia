$namespaces:
  s: http://phenomics.kcl.ac.uk/phenoflow/
baseCommand: node
class: CommandLineTool
cwlVersion: v1.0
doc: Read potential cases from disc
id: read-potential-cases-disc
inputs:
- doc: Node implementation unit
  id: inputModule
  inputBinding:
    position: 1
  type: File
- doc: Potential cases of Abdominal-Hernia
  id: potentialCases
  inputBinding:
    position: 2
  type: File
outputs:
- doc: Initial potential cases, read from disc.
  id: output
  outputBinding:
    glob: '*.csv'
  type: File
requirements:
  DockerRequirement:
    dockerPull: kclhi/node:latest
s:type: load
