FROM projectmonai/monai:latest

ARG PAT=""

RUN mkdir /app /app/data /app/data/input /app/data/output
WORKDIR /app 
RUN git clone https://${PAT}@github.com/kbressem/anterior-mediastinum.git

WORKDIR /app/anterior-mediastinum/bundle
COPY infer.sh /app/anterior-mediastinum/bundle
RUN chmod +x infer.sh
CMD ["./infer.sh"]
LABEL org.nrg.commands="[{\"name\": \"anterior-mediastinum-bundle\", \"description\": \"Run anterior mediastinum segmentation on a scan\", \"label\": \"anterior-mediastinum-segmentation\", \"info-url\": \"\", \"version\": \"0.1\", \"schema-version\": \"1.0\", \"type\": \"docker\", \"runtime\": \"nvidia\", \"gpus\": \"all\", \"image\": \"monai_bundle_inference:0.1\", \"command-line\": \"./infer.sh\", \"mounts\": [{\"name\": \"in\", \"writable\": \"false\", \"path\": \"/app/data/input\"}, {\"name\": \"out\", \"writable\": \"true\", \"path\": \"/app/data/output\"}], \"inputs\": [], \"outputs\": [{\"name\": \"output_files\", \"description\": \"The seg files\", \"mount\": \"out\", \"required\": true}], \"xnat\": [{\"name\": \"anterior-mediastinum-segmentation\", \"description\": \"Run anterior-mediastinum-segmentation on a Scan\", \"label\": \"anterior-mediastinum-segmentation\", \"contexts\": [\"xnat:imageSessionData\"], \"external-inputs\": [{\"name\": \"session\", \"description\": \"Input session\", \"type\": \"Session\", \"required\": true}], \"derived-inputs\": [{\"name\": \"scan\", \"description\": \"Input scan\", \"type\": \"Scan\", \"derived-from-wrapper-input\": \"session\", \"matcher\": \"'DICOM' in @.resources[*].label\"}, {\"name\": \"scan-dicoms\", \"description\": \"The dicom resource on the scan\", \"type\": \"Resource\", \"derived-from-wrapper-input\": \"scan\", \"provides-files-for-command-mount\": \"in\", \"matcher\": \"@.label == 'DICOM'\"}], \"output-handlers\": [{\"name\": \"nrrd\", \"accepts-command-output\": \"output_files\", \"as-a-child-of-wrapper-input\": \"scan\", \"type\": \"Resource\", \"label\": \"Anterior-Mediastinum-Segmentations\"}]}]}]"

