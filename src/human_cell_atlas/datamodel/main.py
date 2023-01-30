# Auto generated from main.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-30T13:25:54
# Schema: hca
#
# id: http://example.org/hca
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AGGREGATE_GENERATION_PROTOCOL = CurieNamespace('Aggregate_generation_protocol', 'https://example.org/Aggregate-generation-protocol')
ANALYSIS_FILE = CurieNamespace('Analysis_file', 'https://example.org/Analysis-file')
ANALYSIS_PROCESS = CurieNamespace('Analysis_process', 'https://example.org/Analysis-process')
ANALYSIS_PROTOCOL = CurieNamespace('Analysis_protocol', 'https://example.org/Analysis-protocol')
BARCODE = CurieNamespace('Barcode', 'https://example.org/Barcode')
BIOLOGICAL_MACROMOLECULE_ONTOLOGY = CurieNamespace('Biological_macromolecule_ontology', 'https://example.org/Biological-macromolecule-ontology')
BIOMATERIAL_CORE = CurieNamespace('Biomaterial_core', 'https://example.org/Biomaterial-core')
CELL_CYCLE_ONTOLOGY = CurieNamespace('Cell_cycle_ontology', 'https://example.org/Cell-cycle-ontology')
CELL_LINE = CurieNamespace('Cell_line', 'https://example.org/Cell-line')
CELL_MORPHOLOGY = CurieNamespace('Cell_morphology', 'https://example.org/Cell-morphology')
CELL_SUSPENSION = CurieNamespace('Cell_suspension', 'https://example.org/Cell-suspension')
CELL_TYPE_ONTOLOGY = CurieNamespace('Cell_type_ontology', 'https://example.org/Cell-type-ontology')
CELLULAR_COMPONENT_ONTOLOGY = CurieNamespace('Cellular_component_ontology', 'https://example.org/Cellular-component-ontology')
CHANNEL = CurieNamespace('Channel', 'https://example.org/Channel')
COLLECTION_PROTOCOL = CurieNamespace('Collection_protocol', 'https://example.org/Collection-protocol')
CONTACT = CurieNamespace('Contact', 'https://example.org/Contact')
CONTRIBUTOR_ROLE_ONTOLOGY = CurieNamespace('Contributor_role_ontology', 'https://example.org/Contributor-role-ontology')
DEATH = CurieNamespace('Death', 'https://example.org/Death')
DEVELOPMENT_STAGE_ONTOLOGY = CurieNamespace('Development_stage_ontology', 'https://example.org/Development-stage-ontology')
DIFFERENTIATION_PROTOCOL = CurieNamespace('Differentiation_protocol', 'https://example.org/Differentiation-protocol')
DISEASE_ONTOLOGY = CurieNamespace('Disease_ontology', 'https://example.org/Disease-ontology')
DISSOCIATION_PROTOCOL = CurieNamespace('Dissociation_protocol', 'https://example.org/Dissociation-protocol')
DONOR_ORGANISM = CurieNamespace('Donor_organism', 'https://example.org/Donor-organism')
ENRICHMENT_ONTOLOGY = CurieNamespace('Enrichment_ontology', 'https://example.org/Enrichment-ontology')
ENRICHMENT_PROTOCOL = CurieNamespace('Enrichment_protocol', 'https://example.org/Enrichment-protocol')
ETHNICITY_ONTOLOGY = CurieNamespace('Ethnicity_ontology', 'https://example.org/Ethnicity-ontology')
FAMILIAL_RELATIONSHIP = CurieNamespace('Familial_relationship', 'https://example.org/Familial-relationship')
FILE_CONTENT_ONTOLOGY = CurieNamespace('File_content_ontology', 'https://example.org/File-content-ontology')
FILE_CORE = CurieNamespace('File_core', 'https://example.org/File-core')
FILE_DESCRIPTOR = CurieNamespace('File_descriptor', 'https://example.org/File-descriptor')
FILE_FORMAT_ONTOLOGY = CurieNamespace('File_format_ontology', 'https://example.org/File-format-ontology')
FUNDER = CurieNamespace('Funder', 'https://example.org/Funder')
GROWTH_CONDITIONS = CurieNamespace('Growth_conditions', 'https://example.org/Growth-conditions')
HUMAN_SPECIFIC = CurieNamespace('Human_specific', 'https://example.org/Human-specific')
INSDC_EXPERIMENT = CurieNamespace('INSDC_experiment', 'https://example.org/INSDC-experiment')
IMAGE_FILE = CurieNamespace('Image_file', 'https://example.org/Image-file')
IMAGED_SPECIMEN = CurieNamespace('Imaged_specimen', 'https://example.org/Imaged-specimen')
IMAGING_PROTOCOL = CurieNamespace('Imaging_Protocol', 'https://example.org/Imaging-Protocol')
IMAGING_PREPARATION_PROTOCOL = CurieNamespace('Imaging_preparation_protocol', 'https://example.org/Imaging-preparation-protocol')
INSTRUMENT_ONTOLOGY = CurieNamespace('Instrument_ontology', 'https://example.org/Instrument-ontology')
LENGTH_UNIT_ONTOLOGY = CurieNamespace('Length_unit_ontology', 'https://example.org/Length-unit-ontology')
LIBRARY_AMPLIFICATION_ONTOLOGY = CurieNamespace('Library_amplification_ontology', 'https://example.org/Library-amplification-ontology')
LIBRARY_CONSTRUCTION_ONTOLOGY = CurieNamespace('Library_construction_ontology', 'https://example.org/Library-construction-ontology')
LIBRARY_PREPARATION_PROTOCOL = CurieNamespace('Library_preparation_protocol', 'https://example.org/Library-preparation-protocol')
LICENSE = CurieNamespace('License', 'https://example.org/License')
LINKS = CurieNamespace('Links', 'https://example.org/Links')
MASS_UNIT_ONTOLOGY = CurieNamespace('Mass_unit_ontology', 'https://example.org/Mass-unit-ontology')
MATRIX = CurieNamespace('Matrix', 'https://example.org/Matrix')
MEDICAL_HISTORY = CurieNamespace('Medical_history', 'https://example.org/Medical-history')
MICROSCOPY_ONTOLOGY = CurieNamespace('Microscopy_ontology', 'https://example.org/Microscopy-ontology')
MOUSE_SPECIFIC = CurieNamespace('Mouse_specific', 'https://example.org/Mouse-specific')
ORGAN_ONTOLOGY = CurieNamespace('Organ_ontology', 'https://example.org/Organ-ontology')
ORGAN_PART_ONTOLOGY = CurieNamespace('Organ_part_ontology', 'https://example.org/Organ-part-ontology')
ORGANOID = CurieNamespace('Organoid', 'https://example.org/Organoid')
PLATE_BASED_SEQUENCING = CurieNamespace('Plate_based_sequencing', 'https://example.org/Plate-based-sequencing')
PRESERVATION_AND_STORAGE = CurieNamespace('Preservation_and_storage', 'https://example.org/Preservation-and-storage')
PROBE = CurieNamespace('Probe', 'https://example.org/Probe')
PROCESS = CurieNamespace('Process', 'https://example.org/Process')
PROCESS_CORE = CurieNamespace('Process_core', 'https://example.org/Process-core')
PROCESS_TYPE_ONTOLOGY = CurieNamespace('Process_type_ontology', 'https://example.org/Process-type-ontology')
PROJECT = CurieNamespace('Project', 'https://example.org/Project')
PROJECT_CORE = CurieNamespace('Project_core', 'https://example.org/Project-core')
PROTOCOL = CurieNamespace('Protocol', 'https://example.org/Protocol')
PROTOCOL_CORE = CurieNamespace('Protocol_core', 'https://example.org/Protocol-core')
PROTOCOL_TYPE_ONTOLOGY = CurieNamespace('Protocol_type_ontology', 'https://example.org/Protocol-type-ontology')
PROVENANCE = CurieNamespace('Provenance', 'https://example.org/Provenance')
PUBLICATION = CurieNamespace('Publication', 'https://example.org/Publication')
PURCHASED_REAGENTS = CurieNamespace('Purchased_reagents', 'https://example.org/Purchased-reagents')
REFERENCE_FILE = CurieNamespace('Reference_file', 'https://example.org/Reference-file')
S10X = CurieNamespace('S10x', 'https://example.org/S10x')
SEQUENCE_FILE = CurieNamespace('Sequence_file', 'https://example.org/Sequence-file')
SEQUENCING_ONTOLOGY = CurieNamespace('Sequencing_ontology', 'https://example.org/Sequencing-ontology')
SEQUENCING_PROTOCOL = CurieNamespace('Sequencing_protocol', 'https://example.org/Sequencing-protocol')
SPECIES_ONTOLOGY = CurieNamespace('Species_ontology', 'https://example.org/Species-ontology')
SPECIMEN_FROM_ORGANISM = CurieNamespace('Specimen_from_organism', 'https://example.org/Specimen-from-organism')
STATE_OF_SPECIMEN = CurieNamespace('State_of_specimen', 'https://example.org/State-of-specimen')
STRAIN_ONTOLOGY = CurieNamespace('Strain_ontology', 'https://example.org/Strain-ontology')
SUPPLEMENTARY_FILE = CurieNamespace('Supplementary_file', 'https://example.org/Supplementary-file')
TARGET_PATHWAY_ONTOLOGY = CurieNamespace('Target_pathway_ontology', 'https://example.org/Target-pathway-ontology')
TIME_UNIT_ONTOLOGY = CurieNamespace('Time_unit_ontology', 'https://example.org/Time-unit-ontology')
TIMECOURSE = CurieNamespace('Timecourse', 'https://example.org/Timecourse')
TREATMENT_METHOD_ONTOLOGY = CurieNamespace('Treatment_method_ontology', 'https://example.org/Treatment-method-ontology')
TREATMENT_PROTOCOL = CurieNamespace('Treatment_protocol', 'https://example.org/Treatment-protocol')
HCA = CurieNamespace('hca', 'http://example.org/hca/')
IPSC_INDUCTION_PROTOCOL = CurieNamespace('iPSC_induction_protocol', 'https://example.org/iPSC-induction-protocol')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = HCA


# Types

# Class references



@dataclass
class FileCore(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FILE_CORE.FileCore
    class_class_curie: ClassVar[str] = "File_core:FileCore"
    class_name: ClassVar[str] = "FileCore"
    class_model_uri: ClassVar[URIRef] = HCA.FileCore

    file_name: str = None
    format: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    content_description: Optional[Union[Union[dict, "FileContentOntology"], List[Union[dict, "FileContentOntology"]]]] = empty_list()
    checksum: Optional[str] = None
    file_source: Optional[Union[str, "FileCoreFileSourceOptions"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        self._normalize_inlined_as_dict(slot_name="content_description", slot_type=FileContentOntology, key_name="text", keyed=False)

        if self.checksum is not None and not isinstance(self.checksum, str):
            self.checksum = str(self.checksum)

        if self.file_source is not None and not isinstance(self.file_source, FileCoreFileSourceOptions):
            self.file_source = FileCoreFileSourceOptions(self.file_source)

        super().__post_init__(**kwargs)


@dataclass
class ProtocolCore(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROTOCOL_CORE.ProtocolCore
    class_class_curie: ClassVar[str] = "Protocol_core:ProtocolCore"
    class_name: ClassVar[str] = "ProtocolCore"
    class_model_uri: ClassVar[URIRef] = HCA.ProtocolCore

    protocol_id: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    protocol_name: Optional[str] = None
    protocol_description: Optional[str] = None
    publication_doi: Optional[str] = None
    protocols_io_doi: Optional[str] = None
    document: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.protocol_id):
            self.MissingRequiredField("protocol_id")
        if not isinstance(self.protocol_id, str):
            self.protocol_id = str(self.protocol_id)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.protocol_name is not None and not isinstance(self.protocol_name, str):
            self.protocol_name = str(self.protocol_name)

        if self.protocol_description is not None and not isinstance(self.protocol_description, str):
            self.protocol_description = str(self.protocol_description)

        if self.publication_doi is not None and not isinstance(self.publication_doi, str):
            self.publication_doi = str(self.publication_doi)

        if self.protocols_io_doi is not None and not isinstance(self.protocols_io_doi, str):
            self.protocols_io_doi = str(self.protocols_io_doi)

        if self.document is not None and not isinstance(self.document, str):
            self.document = str(self.document)

        super().__post_init__(**kwargs)


@dataclass
class ProjectCore(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROJECT_CORE.ProjectCore
    class_class_curie: ClassVar[str] = "Project_core:ProjectCore"
    class_name: ClassVar[str] = "ProjectCore"
    class_model_uri: ClassVar[URIRef] = HCA.ProjectCore

    project_short_name: str = None
    project_title: str = None
    project_description: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.project_short_name):
            self.MissingRequiredField("project_short_name")
        if not isinstance(self.project_short_name, str):
            self.project_short_name = str(self.project_short_name)

        if self._is_empty(self.project_title):
            self.MissingRequiredField("project_title")
        if not isinstance(self.project_title, str):
            self.project_title = str(self.project_title)

        if self._is_empty(self.project_description):
            self.MissingRequiredField("project_description")
        if not isinstance(self.project_description, str):
            self.project_description = str(self.project_description)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        super().__post_init__(**kwargs)


@dataclass
class BiomaterialCore(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOMATERIAL_CORE.BiomaterialCore
    class_class_curie: ClassVar[str] = "Biomaterial_core:BiomaterialCore"
    class_name: ClassVar[str] = "BiomaterialCore"
    class_model_uri: ClassVar[URIRef] = HCA.BiomaterialCore

    biomaterial_id: str = None
    ncbi_taxon_id: Union[int, List[int]] = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    biomaterial_name: Optional[str] = None
    biomaterial_description: Optional[str] = None
    genotype: Optional[str] = None
    supplementary_files: Optional[Union[str, List[str]]] = empty_list()
    biosamples_accession: Optional[str] = None
    insdc_sample_accession: Optional[str] = None
    HDBR_accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.biomaterial_id):
            self.MissingRequiredField("biomaterial_id")
        if not isinstance(self.biomaterial_id, str):
            self.biomaterial_id = str(self.biomaterial_id)

        if self._is_empty(self.ncbi_taxon_id):
            self.MissingRequiredField("ncbi_taxon_id")
        if not isinstance(self.ncbi_taxon_id, list):
            self.ncbi_taxon_id = [self.ncbi_taxon_id] if self.ncbi_taxon_id is not None else []
        self.ncbi_taxon_id = [v if isinstance(v, int) else int(v) for v in self.ncbi_taxon_id]

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.biomaterial_name is not None and not isinstance(self.biomaterial_name, str):
            self.biomaterial_name = str(self.biomaterial_name)

        if self.biomaterial_description is not None and not isinstance(self.biomaterial_description, str):
            self.biomaterial_description = str(self.biomaterial_description)

        if self.genotype is not None and not isinstance(self.genotype, str):
            self.genotype = str(self.genotype)

        if not isinstance(self.supplementary_files, list):
            self.supplementary_files = [self.supplementary_files] if self.supplementary_files is not None else []
        self.supplementary_files = [v if isinstance(v, str) else str(v) for v in self.supplementary_files]

        if self.biosamples_accession is not None and not isinstance(self.biosamples_accession, str):
            self.biosamples_accession = str(self.biosamples_accession)

        if self.insdc_sample_accession is not None and not isinstance(self.insdc_sample_accession, str):
            self.insdc_sample_accession = str(self.insdc_sample_accession)

        if self.HDBR_accession is not None and not isinstance(self.HDBR_accession, str):
            self.HDBR_accession = str(self.HDBR_accession)

        super().__post_init__(**kwargs)


@dataclass
class ProcessCore(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROCESS_CORE.ProcessCore
    class_class_curie: ClassVar[str] = "Process_core:ProcessCore"
    class_name: ClassVar[str] = "ProcessCore"
    class_model_uri: ClassVar[URIRef] = HCA.ProcessCore

    process_id: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    process_name: Optional[str] = None
    process_description: Optional[str] = None
    location: Optional[str] = None
    operators: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.process_id):
            self.MissingRequiredField("process_id")
        if not isinstance(self.process_id, str):
            self.process_id = str(self.process_id)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.process_name is not None and not isinstance(self.process_name, str):
            self.process_name = str(self.process_name)

        if self.process_description is not None and not isinstance(self.process_description, str):
            self.process_description = str(self.process_description)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if not isinstance(self.operators, list):
            self.operators = [self.operators] if self.operators is not None else []
        self.operators = [v if isinstance(v, str) else str(v) for v in self.operators]

        super().__post_init__(**kwargs)


@dataclass
class Channel(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHANNEL.Channel
    class_class_curie: ClassVar[str] = "Channel:Channel"
    class_name: ClassVar[str] = "Channel"
    class_model_uri: ClassVar[URIRef] = HCA.Channel

    channel_id: str = None
    excitation_wavelength: float = None
    filter_range: str = None
    multiplexed: Union[str, "ChannelMultiplexedOptions"] = None
    exposure_time: float = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    target_fluorophore: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.channel_id):
            self.MissingRequiredField("channel_id")
        if not isinstance(self.channel_id, str):
            self.channel_id = str(self.channel_id)

        if self._is_empty(self.excitation_wavelength):
            self.MissingRequiredField("excitation_wavelength")
        if not isinstance(self.excitation_wavelength, float):
            self.excitation_wavelength = float(self.excitation_wavelength)

        if self._is_empty(self.filter_range):
            self.MissingRequiredField("filter_range")
        if not isinstance(self.filter_range, str):
            self.filter_range = str(self.filter_range)

        if self._is_empty(self.multiplexed):
            self.MissingRequiredField("multiplexed")
        if not isinstance(self.multiplexed, ChannelMultiplexedOptions):
            self.multiplexed = ChannelMultiplexedOptions(self.multiplexed)

        if self._is_empty(self.exposure_time):
            self.MissingRequiredField("exposure_time")
        if not isinstance(self.exposure_time, float):
            self.exposure_time = float(self.exposure_time)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.target_fluorophore is not None and not isinstance(self.target_fluorophore, str):
            self.target_fluorophore = str(self.target_fluorophore)

        super().__post_init__(**kwargs)


@dataclass
class Probe(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROBE.Probe
    class_class_curie: ClassVar[str] = "Probe:Probe"
    class_name: ClassVar[str] = "Probe"
    class_model_uri: ClassVar[URIRef] = HCA.Probe

    probe_label: str = None
    target_label: str = None
    assay_type: Union[dict, "ProcessTypeOntology"] = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    probe_sequence: Optional[str] = None
    target_name: Optional[str] = None
    target_codebook_label: Optional[str] = None
    subcellular_structure: Optional[Union[dict, "CellularComponentOntology"]] = None
    probe_reagents: Optional[Union[dict, "PurchasedReagents"]] = None
    fluorophore: Optional[Union[str, List[str]]] = empty_list()
    channel_label: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.probe_label):
            self.MissingRequiredField("probe_label")
        if not isinstance(self.probe_label, str):
            self.probe_label = str(self.probe_label)

        if self._is_empty(self.target_label):
            self.MissingRequiredField("target_label")
        if not isinstance(self.target_label, str):
            self.target_label = str(self.target_label)

        if self._is_empty(self.assay_type):
            self.MissingRequiredField("assay_type")
        if not isinstance(self.assay_type, ProcessTypeOntology):
            self.assay_type = ProcessTypeOntology(**as_dict(self.assay_type))

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.probe_sequence is not None and not isinstance(self.probe_sequence, str):
            self.probe_sequence = str(self.probe_sequence)

        if self.target_name is not None and not isinstance(self.target_name, str):
            self.target_name = str(self.target_name)

        if self.target_codebook_label is not None and not isinstance(self.target_codebook_label, str):
            self.target_codebook_label = str(self.target_codebook_label)

        if self.subcellular_structure is not None and not isinstance(self.subcellular_structure, CellularComponentOntology):
            self.subcellular_structure = CellularComponentOntology(**as_dict(self.subcellular_structure))

        if self.probe_reagents is not None and not isinstance(self.probe_reagents, PurchasedReagents):
            self.probe_reagents = PurchasedReagents(**as_dict(self.probe_reagents))

        if not isinstance(self.fluorophore, list):
            self.fluorophore = [self.fluorophore] if self.fluorophore is not None else []
        self.fluorophore = [v if isinstance(v, str) else str(v) for v in self.fluorophore]

        if not isinstance(self.channel_label, list):
            self.channel_label = [self.channel_label] if self.channel_label is not None else []
        self.channel_label = [v if isinstance(v, str) else str(v) for v in self.channel_label]

        super().__post_init__(**kwargs)


@dataclass
class Matrix(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX.Matrix
    class_class_curie: ClassVar[str] = "Matrix:Matrix"
    class_name: ClassVar[str] = "Matrix"
    class_model_uri: ClassVar[URIRef] = HCA.Matrix

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    data_normalization_methods: Optional[Union[Union[str, "DataNormalizationMethodsOptions"], List[Union[str, "DataNormalizationMethodsOptions"]]]] = empty_list()
    derivation_process: Optional[Union[Union[str, "DerivationProcessOptions"], List[Union[str, "DerivationProcessOptions"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if not isinstance(self.data_normalization_methods, list):
            self.data_normalization_methods = [self.data_normalization_methods] if self.data_normalization_methods is not None else []
        self.data_normalization_methods = [v if isinstance(v, DataNormalizationMethodsOptions) else DataNormalizationMethodsOptions(v) for v in self.data_normalization_methods]

        if not isinstance(self.derivation_process, list):
            self.derivation_process = [self.derivation_process] if self.derivation_process is not None else []
        self.derivation_process = [v if isinstance(v, DerivationProcessOptions) else DerivationProcessOptions(v) for v in self.derivation_process]

        super().__post_init__(**kwargs)


@dataclass
class FileContentOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FILE_CONTENT_ONTOLOGY.FileContentOntology
    class_class_curie: ClassVar[str] = "File_content_ontology:FileContentOntology"
    class_name: ClassVar[str] = "FileContentOntology"
    class_model_uri: ClassVar[URIRef] = HCA.FileContentOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "FileContentOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, FileContentOntologyOntologyOptions):
            self.ontology = FileContentOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class LengthUnitOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LENGTH_UNIT_ONTOLOGY.LengthUnitOntology
    class_class_curie: ClassVar[str] = "Length_unit_ontology:LengthUnitOntology"
    class_name: ClassVar[str] = "LengthUnitOntology"
    class_model_uri: ClassVar[URIRef] = HCA.LengthUnitOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "LengthUnitOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, LengthUnitOntologyOntologyOptions):
            self.ontology = LengthUnitOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class CellCycleOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELL_CYCLE_ONTOLOGY.CellCycleOntology
    class_class_curie: ClassVar[str] = "Cell_cycle_ontology:CellCycleOntology"
    class_name: ClassVar[str] = "CellCycleOntology"
    class_model_uri: ClassVar[URIRef] = HCA.CellCycleOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "CellCycleOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, CellCycleOntologyOntologyOptions):
            self.ontology = CellCycleOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class LibraryAmplificationOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LIBRARY_AMPLIFICATION_ONTOLOGY.LibraryAmplificationOntology
    class_class_curie: ClassVar[str] = "Library_amplification_ontology:LibraryAmplificationOntology"
    class_name: ClassVar[str] = "LibraryAmplificationOntology"
    class_model_uri: ClassVar[URIRef] = HCA.LibraryAmplificationOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "LibraryAmplificationOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, LibraryAmplificationOntologyOntologyOptions):
            self.ontology = LibraryAmplificationOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class ContributorRoleOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTRIBUTOR_ROLE_ONTOLOGY.ContributorRoleOntology
    class_class_curie: ClassVar[str] = "Contributor_role_ontology:ContributorRoleOntology"
    class_name: ClassVar[str] = "ContributorRoleOntology"
    class_model_uri: ClassVar[URIRef] = HCA.ContributorRoleOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "ContributorRoleOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, ContributorRoleOntologyOntologyOptions):
            self.ontology = ContributorRoleOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class EthnicityOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ETHNICITY_ONTOLOGY.EthnicityOntology
    class_class_curie: ClassVar[str] = "Ethnicity_ontology:EthnicityOntology"
    class_name: ClassVar[str] = "EthnicityOntology"
    class_model_uri: ClassVar[URIRef] = HCA.EthnicityOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "EthnicityOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, EthnicityOntologyOntologyOptions):
            self.ontology = EthnicityOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class TargetPathwayOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TARGET_PATHWAY_ONTOLOGY.TargetPathwayOntology
    class_class_curie: ClassVar[str] = "Target_pathway_ontology:TargetPathwayOntology"
    class_name: ClassVar[str] = "TargetPathwayOntology"
    class_model_uri: ClassVar[URIRef] = HCA.TargetPathwayOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "TargetPathwayOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, TargetPathwayOntologyOntologyOptions):
            self.ontology = TargetPathwayOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class TreatmentMethodOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TREATMENT_METHOD_ONTOLOGY.TreatmentMethodOntology
    class_class_curie: ClassVar[str] = "Treatment_method_ontology:TreatmentMethodOntology"
    class_name: ClassVar[str] = "TreatmentMethodOntology"
    class_model_uri: ClassVar[URIRef] = HCA.TreatmentMethodOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "TreatmentMethodOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, TreatmentMethodOntologyOntologyOptions):
            self.ontology = TreatmentMethodOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class CellularComponentOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLULAR_COMPONENT_ONTOLOGY.CellularComponentOntology
    class_class_curie: ClassVar[str] = "Cellular_component_ontology:CellularComponentOntology"
    class_name: ClassVar[str] = "CellularComponentOntology"
    class_model_uri: ClassVar[URIRef] = HCA.CellularComponentOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "CellularComponentOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, CellularComponentOntologyOntologyOptions):
            self.ontology = CellularComponentOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class LibraryConstructionOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LIBRARY_CONSTRUCTION_ONTOLOGY.LibraryConstructionOntology
    class_class_curie: ClassVar[str] = "Library_construction_ontology:LibraryConstructionOntology"
    class_name: ClassVar[str] = "LibraryConstructionOntology"
    class_model_uri: ClassVar[URIRef] = HCA.LibraryConstructionOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "LibraryConstructionOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, LibraryConstructionOntologyOntologyOptions):
            self.ontology = LibraryConstructionOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class ProcessTypeOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROCESS_TYPE_ONTOLOGY.ProcessTypeOntology
    class_class_curie: ClassVar[str] = "Process_type_ontology:ProcessTypeOntology"
    class_name: ClassVar[str] = "ProcessTypeOntology"
    class_model_uri: ClassVar[URIRef] = HCA.ProcessTypeOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "ProcessTypeOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, ProcessTypeOntologyOntologyOptions):
            self.ontology = ProcessTypeOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class SequencingOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEQUENCING_ONTOLOGY.SequencingOntology
    class_class_curie: ClassVar[str] = "Sequencing_ontology:SequencingOntology"
    class_name: ClassVar[str] = "SequencingOntology"
    class_model_uri: ClassVar[URIRef] = HCA.SequencingOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "SequencingOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, SequencingOntologyOntologyOptions):
            self.ontology = SequencingOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class SpeciesOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPECIES_ONTOLOGY.SpeciesOntology
    class_class_curie: ClassVar[str] = "Species_ontology:SpeciesOntology"
    class_name: ClassVar[str] = "SpeciesOntology"
    class_model_uri: ClassVar[URIRef] = HCA.SpeciesOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "SpeciesOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, SpeciesOntologyOntologyOptions):
            self.ontology = SpeciesOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DISEASE_ONTOLOGY.DiseaseOntology
    class_class_curie: ClassVar[str] = "Disease_ontology:DiseaseOntology"
    class_name: ClassVar[str] = "DiseaseOntology"
    class_model_uri: ClassVar[URIRef] = HCA.DiseaseOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "DiseaseOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, DiseaseOntologyOntologyOptions):
            self.ontology = DiseaseOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class StrainOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = STRAIN_ONTOLOGY.StrainOntology
    class_class_curie: ClassVar[str] = "Strain_ontology:StrainOntology"
    class_name: ClassVar[str] = "StrainOntology"
    class_model_uri: ClassVar[URIRef] = HCA.StrainOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "StrainOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, StrainOntologyOntologyOptions):
            self.ontology = StrainOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class FileFormatOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FILE_FORMAT_ONTOLOGY.FileFormatOntology
    class_class_curie: ClassVar[str] = "File_format_ontology:FileFormatOntology"
    class_name: ClassVar[str] = "FileFormatOntology"
    class_model_uri: ClassVar[URIRef] = HCA.FileFormatOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "FileFormatOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, FileFormatOntologyOntologyOptions):
            self.ontology = FileFormatOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class EnrichmentOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ENRICHMENT_ONTOLOGY.EnrichmentOntology
    class_class_curie: ClassVar[str] = "Enrichment_ontology:EnrichmentOntology"
    class_name: ClassVar[str] = "EnrichmentOntology"
    class_model_uri: ClassVar[URIRef] = HCA.EnrichmentOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "EnrichmentOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, EnrichmentOntologyOntologyOptions):
            self.ontology = EnrichmentOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class OrganPartOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGAN_PART_ONTOLOGY.OrganPartOntology
    class_class_curie: ClassVar[str] = "Organ_part_ontology:OrganPartOntology"
    class_name: ClassVar[str] = "OrganPartOntology"
    class_model_uri: ClassVar[URIRef] = HCA.OrganPartOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "OrganPartOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, OrganPartOntologyOntologyOptions):
            self.ontology = OrganPartOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class MicroscopyOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPY_ONTOLOGY.MicroscopyOntology
    class_class_curie: ClassVar[str] = "Microscopy_ontology:MicroscopyOntology"
    class_name: ClassVar[str] = "MicroscopyOntology"
    class_model_uri: ClassVar[URIRef] = HCA.MicroscopyOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "MicroscopyOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, MicroscopyOntologyOntologyOptions):
            self.ontology = MicroscopyOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class TimeUnitOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME_UNIT_ONTOLOGY.TimeUnitOntology
    class_class_curie: ClassVar[str] = "Time_unit_ontology:TimeUnitOntology"
    class_name: ClassVar[str] = "TimeUnitOntology"
    class_model_uri: ClassVar[URIRef] = HCA.TimeUnitOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "TimeUnitOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, TimeUnitOntologyOntologyOptions):
            self.ontology = TimeUnitOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class ProtocolTypeOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROTOCOL_TYPE_ONTOLOGY.ProtocolTypeOntology
    class_class_curie: ClassVar[str] = "Protocol_type_ontology:ProtocolTypeOntology"
    class_name: ClassVar[str] = "ProtocolTypeOntology"
    class_model_uri: ClassVar[URIRef] = HCA.ProtocolTypeOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "ProtocolTypeOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, ProtocolTypeOntologyOntologyOptions):
            self.ontology = ProtocolTypeOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class DevelopmentStageOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DEVELOPMENT_STAGE_ONTOLOGY.DevelopmentStageOntology
    class_class_curie: ClassVar[str] = "Development_stage_ontology:DevelopmentStageOntology"
    class_name: ClassVar[str] = "DevelopmentStageOntology"
    class_model_uri: ClassVar[URIRef] = HCA.DevelopmentStageOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "DevelopmentStageOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, DevelopmentStageOntologyOntologyOptions):
            self.ontology = DevelopmentStageOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class InstrumentOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INSTRUMENT_ONTOLOGY.InstrumentOntology
    class_class_curie: ClassVar[str] = "Instrument_ontology:InstrumentOntology"
    class_name: ClassVar[str] = "InstrumentOntology"
    class_model_uri: ClassVar[URIRef] = HCA.InstrumentOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "InstrumentOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, InstrumentOntologyOntologyOptions):
            self.ontology = InstrumentOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class MassUnitOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MASS_UNIT_ONTOLOGY.MassUnitOntology
    class_class_curie: ClassVar[str] = "Mass_unit_ontology:MassUnitOntology"
    class_name: ClassVar[str] = "MassUnitOntology"
    class_model_uri: ClassVar[URIRef] = HCA.MassUnitOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "MassUnitOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, MassUnitOntologyOntologyOptions):
            self.ontology = MassUnitOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalMacromoleculeOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLOGICAL_MACROMOLECULE_ONTOLOGY.BiologicalMacromoleculeOntology
    class_class_curie: ClassVar[str] = "Biological_macromolecule_ontology:BiologicalMacromoleculeOntology"
    class_name: ClassVar[str] = "BiologicalMacromoleculeOntology"
    class_model_uri: ClassVar[URIRef] = HCA.BiologicalMacromoleculeOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "BiologicalMacromoleculeOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, BiologicalMacromoleculeOntologyOntologyOptions):
            self.ontology = BiologicalMacromoleculeOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class CellTypeOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELL_TYPE_ONTOLOGY.CellTypeOntology
    class_class_curie: ClassVar[str] = "Cell_type_ontology:CellTypeOntology"
    class_name: ClassVar[str] = "CellTypeOntology"
    class_model_uri: ClassVar[URIRef] = HCA.CellTypeOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "CellTypeOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, CellTypeOntologyOntologyOptions):
            self.ontology = CellTypeOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class OrganOntology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGAN_ONTOLOGY.OrganOntology
    class_class_curie: ClassVar[str] = "Organ_ontology:OrganOntology"
    class_name: ClassVar[str] = "OrganOntology"
    class_model_uri: ClassVar[URIRef] = HCA.OrganOntology

    text: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    ontology: Optional[Union[str, "OrganOntologyOntologyOptions"]] = None
    ontology_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.ontology is not None and not isinstance(self.ontology, OrganOntologyOntologyOptions):
            self.ontology = OrganOntologyOntologyOptions(self.ontology)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        super().__post_init__(**kwargs)


@dataclass
class Funder(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FUNDER.Funder
    class_class_curie: ClassVar[str] = "Funder:Funder"
    class_name: ClassVar[str] = "Funder"
    class_model_uri: ClassVar[URIRef] = HCA.Funder

    grant_id: str = None
    organization: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    grant_title: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.grant_id):
            self.MissingRequiredField("grant_id")
        if not isinstance(self.grant_id, str):
            self.grant_id = str(self.grant_id)

        if self._is_empty(self.organization):
            self.MissingRequiredField("organization")
        if not isinstance(self.organization, str):
            self.organization = str(self.organization)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.grant_title is not None and not isinstance(self.grant_title, str):
            self.grant_title = str(self.grant_title)

        super().__post_init__(**kwargs)


@dataclass
class Contact(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTACT.Contact
    class_class_curie: ClassVar[str] = "Contact:Contact"
    class_name: ClassVar[str] = "Contact"
    class_model_uri: ClassVar[URIRef] = HCA.Contact

    institution: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    laboratory: Optional[str] = None
    address: Optional[str] = None
    country: Optional[str] = None
    corresponding_contributor: Optional[Union[bool, Bool]] = None
    project_role: Optional[Union[dict, ContributorRoleOntology]] = None
    orcid_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.institution):
            self.MissingRequiredField("institution")
        if not isinstance(self.institution, str):
            self.institution = str(self.institution)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.phone is not None and not isinstance(self.phone, str):
            self.phone = str(self.phone)

        if self.laboratory is not None and not isinstance(self.laboratory, str):
            self.laboratory = str(self.laboratory)

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.corresponding_contributor is not None and not isinstance(self.corresponding_contributor, Bool):
            self.corresponding_contributor = Bool(self.corresponding_contributor)

        if self.project_role is not None and not isinstance(self.project_role, ContributorRoleOntology):
            self.project_role = ContributorRoleOntology(**as_dict(self.project_role))

        if self.orcid_id is not None and not isinstance(self.orcid_id, str):
            self.orcid_id = str(self.orcid_id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PUBLICATION.Publication
    class_class_curie: ClassVar[str] = "Publication:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = HCA.Publication

    authors: Union[str, List[str]] = None
    title: str = None
    official_hca_publication: Union[bool, Bool] = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    doi: Optional[str] = None
    pmid: Optional[int] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.authors):
            self.MissingRequiredField("authors")
        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.official_hca_publication):
            self.MissingRequiredField("official_hca_publication")
        if not isinstance(self.official_hca_publication, Bool):
            self.official_hca_publication = Bool(self.official_hca_publication)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if self.pmid is not None and not isinstance(self.pmid, int):
            self.pmid = int(self.pmid)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass
class HumanSpecific(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HUMAN_SPECIFIC.HumanSpecific
    class_class_curie: ClassVar[str] = "Human_specific:HumanSpecific"
    class_name: ClassVar[str] = "HumanSpecific"
    class_model_uri: ClassVar[URIRef] = HCA.HumanSpecific

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    body_mass_index: Optional[float] = None
    ethnicity: Optional[Union[Union[dict, EthnicityOntology], List[Union[dict, EthnicityOntology]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.body_mass_index is not None and not isinstance(self.body_mass_index, float):
            self.body_mass_index = float(self.body_mass_index)

        self._normalize_inlined_as_dict(slot_name="ethnicity", slot_type=EthnicityOntology, key_name="text", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class GrowthConditions(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GROWTH_CONDITIONS.GrowthConditions
    class_class_curie: ClassVar[str] = "Growth_conditions:GrowthConditions"
    class_name: ClassVar[str] = "GrowthConditions"
    class_model_uri: ClassVar[URIRef] = HCA.GrowthConditions

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    passage_number: Optional[int] = None
    growth_medium: Optional[str] = None
    culture_environment: Optional[str] = None
    mycoplasma_testing_method: Optional[Union[str, "GrowthConditionsMycoplasmaTestingMethodOptions"]] = None
    mycoplasma_testing_results: Optional[Union[str, "GrowthConditionsMycoplasmaTestingResultsOptions"]] = None
    drug_treatment: Optional[str] = None
    feeder_layer_type: Optional[Union[str, "GrowthConditionsFeederLayerTypeOptions"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.growth_medium is not None and not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self.culture_environment is not None and not isinstance(self.culture_environment, str):
            self.culture_environment = str(self.culture_environment)

        if self.mycoplasma_testing_method is not None and not isinstance(self.mycoplasma_testing_method, GrowthConditionsMycoplasmaTestingMethodOptions):
            self.mycoplasma_testing_method = GrowthConditionsMycoplasmaTestingMethodOptions(self.mycoplasma_testing_method)

        if self.mycoplasma_testing_results is not None and not isinstance(self.mycoplasma_testing_results, GrowthConditionsMycoplasmaTestingResultsOptions):
            self.mycoplasma_testing_results = GrowthConditionsMycoplasmaTestingResultsOptions(self.mycoplasma_testing_results)

        if self.drug_treatment is not None and not isinstance(self.drug_treatment, str):
            self.drug_treatment = str(self.drug_treatment)

        if self.feeder_layer_type is not None and not isinstance(self.feeder_layer_type, GrowthConditionsFeederLayerTypeOptions):
            self.feeder_layer_type = GrowthConditionsFeederLayerTypeOptions(self.feeder_layer_type)

        super().__post_init__(**kwargs)


@dataclass
class PreservationStorage(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PRESERVATION_AND_STORAGE.PreservationStorage
    class_class_curie: ClassVar[str] = "Preservation_and_storage:PreservationStorage"
    class_name: ClassVar[str] = "PreservationStorage"
    class_model_uri: ClassVar[URIRef] = HCA.PreservationStorage

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    storage_method: Optional[Union[str, "PreservationStorageStorageMethodOptions"]] = None
    storage_time: Optional[float] = None
    storage_time_unit: Optional[Union[dict, TimeUnitOntology]] = None
    preservation_method: Optional[Union[str, "PreservationStoragePreservationMethodOptions"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.storage_method is not None and not isinstance(self.storage_method, PreservationStorageStorageMethodOptions):
            self.storage_method = PreservationStorageStorageMethodOptions(self.storage_method)

        if self.storage_time is not None and not isinstance(self.storage_time, float):
            self.storage_time = float(self.storage_time)

        if self.storage_time_unit is not None and not isinstance(self.storage_time_unit, TimeUnitOntology):
            self.storage_time_unit = TimeUnitOntology(**as_dict(self.storage_time_unit))

        if self.preservation_method is not None and not isinstance(self.preservation_method, PreservationStoragePreservationMethodOptions):
            self.preservation_method = PreservationStoragePreservationMethodOptions(self.preservation_method)

        super().__post_init__(**kwargs)


@dataclass
class Death(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DEATH.Death
    class_class_curie: ClassVar[str] = "Death:Death"
    class_name: ClassVar[str] = "Death"
    class_model_uri: ClassVar[URIRef] = HCA.Death

    cause_of_death: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    cold_perfused: Optional[Union[bool, Bool]] = None
    days_on_ventilator: Optional[float] = None
    hardy_scale: Optional[int] = None
    time_of_death: Optional[str] = None
    organ_donation_death_type: Optional[Union[str, "DeathOrganDonationDeathTypeOptions"]] = None
    normothermic_regional_perfusion: Optional[Union[str, "DeathNormothermicRegionalPerfusionOptions"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cause_of_death):
            self.MissingRequiredField("cause_of_death")
        if not isinstance(self.cause_of_death, str):
            self.cause_of_death = str(self.cause_of_death)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.cold_perfused is not None and not isinstance(self.cold_perfused, Bool):
            self.cold_perfused = Bool(self.cold_perfused)

        if self.days_on_ventilator is not None and not isinstance(self.days_on_ventilator, float):
            self.days_on_ventilator = float(self.days_on_ventilator)

        if self.hardy_scale is not None and not isinstance(self.hardy_scale, int):
            self.hardy_scale = int(self.hardy_scale)

        if self.time_of_death is not None and not isinstance(self.time_of_death, str):
            self.time_of_death = str(self.time_of_death)

        if self.organ_donation_death_type is not None and not isinstance(self.organ_donation_death_type, DeathOrganDonationDeathTypeOptions):
            self.organ_donation_death_type = DeathOrganDonationDeathTypeOptions(self.organ_donation_death_type)

        if self.normothermic_regional_perfusion is not None and not isinstance(self.normothermic_regional_perfusion, DeathNormothermicRegionalPerfusionOptions):
            self.normothermic_regional_perfusion = DeathNormothermicRegionalPerfusionOptions(self.normothermic_regional_perfusion)

        super().__post_init__(**kwargs)


@dataclass
class FamilialRelationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FAMILIAL_RELATIONSHIP.FamilialRelationship
    class_class_curie: ClassVar[str] = "Familial_relationship:FamilialRelationship"
    class_name: ClassVar[str] = "FamilialRelationship"
    class_model_uri: ClassVar[URIRef] = HCA.FamilialRelationship

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    parent: Optional[str] = None
    child: Optional[str] = None
    sibling: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.parent is not None and not isinstance(self.parent, str):
            self.parent = str(self.parent)

        if self.child is not None and not isinstance(self.child, str):
            self.child = str(self.child)

        if self.sibling is not None and not isinstance(self.sibling, str):
            self.sibling = str(self.sibling)

        super().__post_init__(**kwargs)


@dataclass
class MedicalHistory(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MEDICAL_HISTORY.MedicalHistory
    class_class_curie: ClassVar[str] = "Medical_history:MedicalHistory"
    class_name: ClassVar[str] = "MedicalHistory"
    class_model_uri: ClassVar[URIRef] = HCA.MedicalHistory

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    alcohol_history: Optional[str] = None
    medication: Optional[str] = None
    smoking_history: Optional[str] = None
    nutritional_state: Optional[Union[str, "MedicalHistoryNutritionalStateOptions"]] = None
    test_results: Optional[str] = None
    treatment: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.alcohol_history is not None and not isinstance(self.alcohol_history, str):
            self.alcohol_history = str(self.alcohol_history)

        if self.medication is not None and not isinstance(self.medication, str):
            self.medication = str(self.medication)

        if self.smoking_history is not None and not isinstance(self.smoking_history, str):
            self.smoking_history = str(self.smoking_history)

        if self.nutritional_state is not None and not isinstance(self.nutritional_state, MedicalHistoryNutritionalStateOptions):
            self.nutritional_state = MedicalHistoryNutritionalStateOptions(self.nutritional_state)

        if self.test_results is not None and not isinstance(self.test_results, str):
            self.test_results = str(self.test_results)

        if self.treatment is not None and not isinstance(self.treatment, str):
            self.treatment = str(self.treatment)

        super().__post_init__(**kwargs)


@dataclass
class CellMorphology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELL_MORPHOLOGY.CellMorphology
    class_class_curie: ClassVar[str] = "Cell_morphology:CellMorphology"
    class_name: ClassVar[str] = "CellMorphology"
    class_model_uri: ClassVar[URIRef] = HCA.CellMorphology

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    cell_morphology: Optional[str] = None
    cell_size: Optional[str] = None
    cell_size_unit: Optional[Union[dict, LengthUnitOntology]] = None
    percent_cell_viability: Optional[float] = None
    cell_viability_method: Optional[str] = None
    cell_viability_result: Optional[Union[str, "CellMorphologyCellViabilityResultOptions"]] = None
    percent_necrosis: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.cell_morphology is not None and not isinstance(self.cell_morphology, str):
            self.cell_morphology = str(self.cell_morphology)

        if self.cell_size is not None and not isinstance(self.cell_size, str):
            self.cell_size = str(self.cell_size)

        if self.cell_size_unit is not None and not isinstance(self.cell_size_unit, LengthUnitOntology):
            self.cell_size_unit = LengthUnitOntology(**as_dict(self.cell_size_unit))

        if self.percent_cell_viability is not None and not isinstance(self.percent_cell_viability, float):
            self.percent_cell_viability = float(self.percent_cell_viability)

        if self.cell_viability_method is not None and not isinstance(self.cell_viability_method, str):
            self.cell_viability_method = str(self.cell_viability_method)

        if self.cell_viability_result is not None and not isinstance(self.cell_viability_result, CellMorphologyCellViabilityResultOptions):
            self.cell_viability_result = CellMorphologyCellViabilityResultOptions(self.cell_viability_result)

        if self.percent_necrosis is not None and not isinstance(self.percent_necrosis, float):
            self.percent_necrosis = float(self.percent_necrosis)

        super().__post_init__(**kwargs)


@dataclass
class StateOfSpecimen(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = STATE_OF_SPECIMEN.StateOfSpecimen
    class_class_curie: ClassVar[str] = "State_of_specimen:StateOfSpecimen"
    class_name: ClassVar[str] = "StateOfSpecimen"
    class_model_uri: ClassVar[URIRef] = HCA.StateOfSpecimen

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    autolysis_score: Optional[Union[str, "StateOfSpecimenAutolysisScoreOptions"]] = None
    gross_description: Optional[str] = None
    gross_images: Optional[Union[str, List[str]]] = empty_list()
    ischemic_temperature: Optional[Union[str, "StateOfSpecimenIschemicTemperatureOptions"]] = None
    ischemic_time: Optional[int] = None
    microscopic_description: Optional[str] = None
    microscopic_images: Optional[Union[str, List[str]]] = empty_list()
    postmortem_interval: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.autolysis_score is not None and not isinstance(self.autolysis_score, StateOfSpecimenAutolysisScoreOptions):
            self.autolysis_score = StateOfSpecimenAutolysisScoreOptions(self.autolysis_score)

        if self.gross_description is not None and not isinstance(self.gross_description, str):
            self.gross_description = str(self.gross_description)

        if not isinstance(self.gross_images, list):
            self.gross_images = [self.gross_images] if self.gross_images is not None else []
        self.gross_images = [v if isinstance(v, str) else str(v) for v in self.gross_images]

        if self.ischemic_temperature is not None and not isinstance(self.ischemic_temperature, StateOfSpecimenIschemicTemperatureOptions):
            self.ischemic_temperature = StateOfSpecimenIschemicTemperatureOptions(self.ischemic_temperature)

        if self.ischemic_time is not None and not isinstance(self.ischemic_time, int):
            self.ischemic_time = int(self.ischemic_time)

        if self.microscopic_description is not None and not isinstance(self.microscopic_description, str):
            self.microscopic_description = str(self.microscopic_description)

        if not isinstance(self.microscopic_images, list):
            self.microscopic_images = [self.microscopic_images] if self.microscopic_images is not None else []
        self.microscopic_images = [v if isinstance(v, str) else str(v) for v in self.microscopic_images]

        if self.postmortem_interval is not None and not isinstance(self.postmortem_interval, int):
            self.postmortem_interval = int(self.postmortem_interval)

        super().__post_init__(**kwargs)


@dataclass
class Timecourse(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIMECOURSE.Timecourse
    class_class_curie: ClassVar[str] = "Timecourse:Timecourse"
    class_name: ClassVar[str] = "Timecourse"
    class_model_uri: ClassVar[URIRef] = HCA.Timecourse

    value: str = None
    unit: Union[dict, TimeUnitOntology] = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    relevance: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, TimeUnitOntology):
            self.unit = TimeUnitOntology(**as_dict(self.unit))

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.relevance is not None and not isinstance(self.relevance, str):
            self.relevance = str(self.relevance)

        super().__post_init__(**kwargs)


@dataclass
class MouseSpecific(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MOUSE_SPECIFIC.MouseSpecific
    class_class_curie: ClassVar[str] = "Mouse_specific:MouseSpecific"
    class_name: ClassVar[str] = "MouseSpecific"
    class_model_uri: ClassVar[URIRef] = HCA.MouseSpecific

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    strain: Optional[Union[Union[dict, StrainOntology], List[Union[dict, StrainOntology]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        self._normalize_inlined_as_dict(slot_name="strain", slot_type=StrainOntology, key_name="text", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class PurchasedReagents(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PURCHASED_REAGENTS.PurchasedReagents
    class_class_curie: ClassVar[str] = "Purchased_reagents:PurchasedReagents"
    class_name: ClassVar[str] = "PurchasedReagents"
    class_model_uri: ClassVar[URIRef] = HCA.PurchasedReagents

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    retail_name: Optional[str] = None
    catalog_number: Optional[str] = None
    manufacturer: Optional[str] = None
    lot_number: Optional[str] = None
    expiry_date: Optional[str] = None
    kit_titer: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.retail_name is not None and not isinstance(self.retail_name, str):
            self.retail_name = str(self.retail_name)

        if self.catalog_number is not None and not isinstance(self.catalog_number, str):
            self.catalog_number = str(self.catalog_number)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.lot_number is not None and not isinstance(self.lot_number, str):
            self.lot_number = str(self.lot_number)

        if self.expiry_date is not None and not isinstance(self.expiry_date, str):
            self.expiry_date = str(self.expiry_date)

        if self.kit_titer is not None and not isinstance(self.kit_titer, str):
            self.kit_titer = str(self.kit_titer)

        super().__post_init__(**kwargs)


@dataclass
class InsdcExperiment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INSDC_EXPERIMENT.InsdcExperiment
    class_class_curie: ClassVar[str] = "INSDC_experiment:InsdcExperiment"
    class_name: ClassVar[str] = "InsdcExperiment"
    class_model_uri: ClassVar[URIRef] = HCA.InsdcExperiment

    insdc_experiment_accession: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.insdc_experiment_accession):
            self.MissingRequiredField("insdc_experiment_accession")
        if not isinstance(self.insdc_experiment_accession, str):
            self.insdc_experiment_accession = str(self.insdc_experiment_accession)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        super().__post_init__(**kwargs)


@dataclass
class Barcode(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BARCODE.Barcode
    class_class_curie: ClassVar[str] = "Barcode:Barcode"
    class_name: ClassVar[str] = "Barcode"
    class_model_uri: ClassVar[URIRef] = HCA.Barcode

    barcode_read: Union[str, "BarcodeBarcodeReadOptions"] = None
    barcode_offset: int = None
    barcode_length: int = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    white_list_file: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.barcode_read):
            self.MissingRequiredField("barcode_read")
        if not isinstance(self.barcode_read, BarcodeBarcodeReadOptions):
            self.barcode_read = BarcodeBarcodeReadOptions(self.barcode_read)

        if self._is_empty(self.barcode_offset):
            self.MissingRequiredField("barcode_offset")
        if not isinstance(self.barcode_offset, int):
            self.barcode_offset = int(self.barcode_offset)

        if self._is_empty(self.barcode_length):
            self.MissingRequiredField("barcode_length")
        if not isinstance(self.barcode_length, int):
            self.barcode_length = int(self.barcode_length)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.white_list_file is not None and not isinstance(self.white_list_file, str):
            self.white_list_file = str(self.white_list_file)

        super().__post_init__(**kwargs)


@dataclass
class S10x(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = S10X.S10x
    class_class_curie: ClassVar[str] = "S10x:S10x"
    class_name: ClassVar[str] = "S10x"
    class_model_uri: ClassVar[URIRef] = HCA.S10x

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    fastq_method: Optional[str] = None
    fastq_method_version: Optional[str] = None
    pooled_channels: Optional[float] = None
    drop_uniformity: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.fastq_method is not None and not isinstance(self.fastq_method, str):
            self.fastq_method = str(self.fastq_method)

        if self.fastq_method_version is not None and not isinstance(self.fastq_method_version, str):
            self.fastq_method_version = str(self.fastq_method_version)

        if self.pooled_channels is not None and not isinstance(self.pooled_channels, float):
            self.pooled_channels = float(self.pooled_channels)

        if self.drop_uniformity is not None and not isinstance(self.drop_uniformity, Bool):
            self.drop_uniformity = Bool(self.drop_uniformity)

        super().__post_init__(**kwargs)


@dataclass
class PlateBasedSequencing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLATE_BASED_SEQUENCING.PlateBasedSequencing
    class_class_curie: ClassVar[str] = "Plate_based_sequencing:PlateBasedSequencing"
    class_name: ClassVar[str] = "PlateBasedSequencing"
    class_model_uri: ClassVar[URIRef] = HCA.PlateBasedSequencing

    plate_label: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    well_label: Optional[str] = None
    well_quality: Optional[Union[str, "PlateBasedSequencingWellQualityOptions"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.plate_label):
            self.MissingRequiredField("plate_label")
        if not isinstance(self.plate_label, str):
            self.plate_label = str(self.plate_label)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.well_label is not None and not isinstance(self.well_label, str):
            self.well_label = str(self.well_label)

        if self.well_quality is not None and not isinstance(self.well_quality, PlateBasedSequencingWellQualityOptions):
            self.well_quality = PlateBasedSequencingWellQualityOptions(self.well_quality)

        super().__post_init__(**kwargs)


@dataclass
class Provenance(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROVENANCE.Provenance
    class_class_curie: ClassVar[str] = "Provenance:Provenance"
    class_name: ClassVar[str] = "Provenance"
    class_model_uri: ClassVar[URIRef] = HCA.Provenance

    submission_date: str = None
    document_id: str = None
    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    schema_major_version: Optional[int] = None
    schema_minor_version: Optional[int] = None
    submitter_id: Optional[str] = None
    update_date: Optional[str] = None
    updater_id: Optional[str] = None
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.submission_date):
            self.MissingRequiredField("submission_date")
        if not isinstance(self.submission_date, str):
            self.submission_date = str(self.submission_date)

        if self._is_empty(self.document_id):
            self.MissingRequiredField("document_id")
        if not isinstance(self.document_id, str):
            self.document_id = str(self.document_id)

        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.schema_major_version is not None and not isinstance(self.schema_major_version, int):
            self.schema_major_version = int(self.schema_major_version)

        if self.schema_minor_version is not None and not isinstance(self.schema_minor_version, int):
            self.schema_minor_version = int(self.schema_minor_version)

        if self.submitter_id is not None and not isinstance(self.submitter_id, str):
            self.submitter_id = str(self.submitter_id)

        if self.update_date is not None and not isinstance(self.update_date, str):
            self.update_date = str(self.update_date)

        if self.updater_id is not None and not isinstance(self.updater_id, str):
            self.updater_id = str(self.updater_id)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class FileDescriptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FILE_DESCRIPTOR.FileDescriptor
    class_class_curie: ClassVar[str] = "File_descriptor:FileDescriptor"
    class_name: ClassVar[str] = "FileDescriptor"
    class_model_uri: ClassVar[URIRef] = HCA.FileDescriptor

    describedBy: str = None
    schema_type: Union[str, "FileDescriptorSchemaTypeOptions"] = None
    file_name: str = None
    file_id: str = None
    file_version: str = None
    content_type: str = None
    size: int = None
    sha256: str = None
    crc32c: str = None
    schema_version: Optional[str] = None
    sha1: Optional[str] = None
    s3_etag: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, FileDescriptorSchemaTypeOptions):
            self.schema_type = FileDescriptorSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.file_id):
            self.MissingRequiredField("file_id")
        if not isinstance(self.file_id, str):
            self.file_id = str(self.file_id)

        if self._is_empty(self.file_version):
            self.MissingRequiredField("file_version")
        if not isinstance(self.file_version, str):
            self.file_version = str(self.file_version)

        if self._is_empty(self.content_type):
            self.MissingRequiredField("content_type")
        if not isinstance(self.content_type, str):
            self.content_type = str(self.content_type)

        if self._is_empty(self.size):
            self.MissingRequiredField("size")
        if not isinstance(self.size, int):
            self.size = int(self.size)

        if self._is_empty(self.sha256):
            self.MissingRequiredField("sha256")
        if not isinstance(self.sha256, str):
            self.sha256 = str(self.sha256)

        if self._is_empty(self.crc32c):
            self.MissingRequiredField("crc32c")
        if not isinstance(self.crc32c, str):
            self.crc32c = str(self.crc32c)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.sha1 is not None and not isinstance(self.sha1, str):
            self.sha1 = str(self.sha1)

        if self.s3_etag is not None and not isinstance(self.s3_etag, str):
            self.s3_etag = str(self.s3_etag)

        super().__post_init__(**kwargs)


@dataclass
class Input(YAMLRoot):
    """
    An input to a process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKS.Input
    class_class_curie: ClassVar[str] = "Links:Input"
    class_name: ClassVar[str] = "Input"
    class_model_uri: ClassVar[URIRef] = HCA.Input

    input_type: str = None
    input_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.input_type):
            self.MissingRequiredField("input_type")
        if not isinstance(self.input_type, str):
            self.input_type = str(self.input_type)

        if self._is_empty(self.input_id):
            self.MissingRequiredField("input_id")
        if not isinstance(self.input_id, str):
            self.input_id = str(self.input_id)

        super().__post_init__(**kwargs)


@dataclass
class Output(YAMLRoot):
    """
    An output from a process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKS.Output
    class_class_curie: ClassVar[str] = "Links:Output"
    class_name: ClassVar[str] = "Output"
    class_model_uri: ClassVar[URIRef] = HCA.Output

    output_type: str = None
    output_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.output_type):
            self.MissingRequiredField("output_type")
        if not isinstance(self.output_type, str):
            self.output_type = str(self.output_type)

        if self._is_empty(self.output_id):
            self.MissingRequiredField("output_id")
        if not isinstance(self.output_id, str):
            self.output_id = str(self.output_id)

        super().__post_init__(**kwargs)


@dataclass
class ProtocolReference(YAMLRoot):
    """
    A protocol used in a process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKS.ProtocolReference
    class_class_curie: ClassVar[str] = "Links:ProtocolReference"
    class_name: ClassVar[str] = "ProtocolReference"
    class_model_uri: ClassVar[URIRef] = HCA.ProtocolReference

    protocol_type: Union[str, "ProtocolReferenceProtocolTypeOptions"] = None
    protocol_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.protocol_type):
            self.MissingRequiredField("protocol_type")
        if not isinstance(self.protocol_type, ProtocolReferenceProtocolTypeOptions):
            self.protocol_type = ProtocolReferenceProtocolTypeOptions(self.protocol_type)

        if self._is_empty(self.protocol_id):
            self.MissingRequiredField("protocol_id")
        if not isinstance(self.protocol_id, str):
            self.protocol_id = str(self.protocol_id)

        super().__post_init__(**kwargs)


@dataclass
class ProcessLink(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKS.ProcessLink
    class_class_curie: ClassVar[str] = "Links:ProcessLink"
    class_name: ClassVar[str] = "ProcessLink"
    class_model_uri: ClassVar[URIRef] = HCA.ProcessLink

    process_type: str = None
    process_id: str = None
    inputs: Union[Union[dict, Input], List[Union[dict, Input]]] = None
    outputs: Union[Union[dict, Output], List[Union[dict, Output]]] = None
    protocols: Union[Union[dict, ProtocolReference], List[Union[dict, ProtocolReference]]] = None
    link_type: Union[str, "ProcessLinkLinkTypeOptions"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.process_type):
            self.MissingRequiredField("process_type")
        if not isinstance(self.process_type, str):
            self.process_type = str(self.process_type)

        if self._is_empty(self.process_id):
            self.MissingRequiredField("process_id")
        if not isinstance(self.process_id, str):
            self.process_id = str(self.process_id)

        if self._is_empty(self.inputs):
            self.MissingRequiredField("inputs")
        self._normalize_inlined_as_dict(slot_name="inputs", slot_type=Input, key_name="input_type", keyed=False)

        if self._is_empty(self.outputs):
            self.MissingRequiredField("outputs")
        self._normalize_inlined_as_dict(slot_name="outputs", slot_type=Output, key_name="output_type", keyed=False)

        if self._is_empty(self.protocols):
            self.MissingRequiredField("protocols")
        self._normalize_inlined_as_dict(slot_name="protocols", slot_type=ProtocolReference, key_name="protocol_type", keyed=False)

        if self._is_empty(self.link_type):
            self.MissingRequiredField("link_type")
        if not isinstance(self.link_type, ProcessLinkLinkTypeOptions):
            self.link_type = ProcessLinkLinkTypeOptions(self.link_type)

        super().__post_init__(**kwargs)


@dataclass
class SupplementaryFileEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKS.SupplementaryFileEntity
    class_class_curie: ClassVar[str] = "Links:SupplementaryFileEntity"
    class_name: ClassVar[str] = "SupplementaryFileEntity"
    class_model_uri: ClassVar[URIRef] = HCA.SupplementaryFileEntity

    file_id: str = None
    file_type: Union[str, "SupplementaryFileEntityFileTypeOptions"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.file_id):
            self.MissingRequiredField("file_id")
        if not isinstance(self.file_id, str):
            self.file_id = str(self.file_id)

        if self._is_empty(self.file_type):
            self.MissingRequiredField("file_type")
        if not isinstance(self.file_type, SupplementaryFileEntityFileTypeOptions):
            self.file_type = SupplementaryFileEntityFileTypeOptions(self.file_type)

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKS.Entity
    class_class_curie: ClassVar[str] = "Links:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = HCA.Entity

    entity_id: str = None
    entity_type: Union[str, "EntityEntityTypeOptions"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.entity_id):
            self.MissingRequiredField("entity_id")
        if not isinstance(self.entity_id, str):
            self.entity_id = str(self.entity_id)

        if self._is_empty(self.entity_type):
            self.MissingRequiredField("entity_type")
        if not isinstance(self.entity_type, EntityEntityTypeOptions):
            self.entity_type = EntityEntityTypeOptions(self.entity_type)

        super().__post_init__(**kwargs)


@dataclass
class SupplementaryFileLink(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKS.SupplementaryFileLink
    class_class_curie: ClassVar[str] = "Links:SupplementaryFileLink"
    class_name: ClassVar[str] = "SupplementaryFileLink"
    class_model_uri: ClassVar[URIRef] = HCA.SupplementaryFileLink

    entity: Union[dict, Entity] = None
    files: Union[Union[dict, "SupplementaryFile"], List[Union[dict, "SupplementaryFile"]]] = None
    link_type: Union[str, "SupplementaryFileLinkLinkTypeOptions"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.entity):
            self.MissingRequiredField("entity")
        if not isinstance(self.entity, Entity):
            self.entity = Entity(**as_dict(self.entity))

        if self._is_empty(self.files):
            self.MissingRequiredField("files")
        self._normalize_inlined_as_dict(slot_name="files", slot_type=SupplementaryFile, key_name="describedBy", keyed=False)

        if self._is_empty(self.link_type):
            self.MissingRequiredField("link_type")
        if not isinstance(self.link_type, SupplementaryFileLinkLinkTypeOptions):
            self.link_type = SupplementaryFileLinkLinkTypeOptions(self.link_type)

        super().__post_init__(**kwargs)


@dataclass
class Links(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKS.Links
    class_class_curie: ClassVar[str] = "Links:Links"
    class_name: ClassVar[str] = "Links"
    class_model_uri: ClassVar[URIRef] = HCA.Links

    describedBy: str = None
    schema_type: Union[str, "LinksSchemaTypeOptions"] = None
    links: Union[str, List[str]] = None
    schema_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, LinksSchemaTypeOptions):
            self.schema_type = LinksSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.links):
            self.MissingRequiredField("links")
        if not isinstance(self.links, list):
            self.links = [self.links] if self.links is not None else []
        self.links = [v if isinstance(v, str) else str(v) for v in self.links]

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        super().__post_init__(**kwargs)


@dataclass
class License(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LICENSE.License
    class_class_curie: ClassVar[str] = "License:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = HCA.License

    describedBy: Optional[str] = None
    schema_version: Optional[str] = None
    identifier: Optional[str] = None
    full_name: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describedBy is not None and not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.full_name is not None and not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass
class SequenceFile(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEQUENCE_FILE.SequenceFile
    class_class_curie: ClassVar[str] = "Sequence_file:SequenceFile"
    class_name: ClassVar[str] = "SequenceFile"
    class_model_uri: ClassVar[URIRef] = HCA.SequenceFile

    describedBy: str = None
    schema_type: Union[str, "SequenceFileSchemaTypeOptions"] = None
    file_core: Union[dict, FileCore] = None
    read_index: Union[str, "SequenceFileReadIndexOptions"] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    lane_index: Optional[int] = None
    read_length: Optional[int] = None
    insdc_run_accessions: Optional[Union[str, List[str]]] = empty_list()
    library_prep_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, SequenceFileSchemaTypeOptions):
            self.schema_type = SequenceFileSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.file_core):
            self.MissingRequiredField("file_core")
        if not isinstance(self.file_core, FileCore):
            self.file_core = FileCore(**as_dict(self.file_core))

        if self._is_empty(self.read_index):
            self.MissingRequiredField("read_index")
        if not isinstance(self.read_index, SequenceFileReadIndexOptions):
            self.read_index = SequenceFileReadIndexOptions(self.read_index)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.lane_index is not None and not isinstance(self.lane_index, int):
            self.lane_index = int(self.lane_index)

        if self.read_length is not None and not isinstance(self.read_length, int):
            self.read_length = int(self.read_length)

        if not isinstance(self.insdc_run_accessions, list):
            self.insdc_run_accessions = [self.insdc_run_accessions] if self.insdc_run_accessions is not None else []
        self.insdc_run_accessions = [v if isinstance(v, str) else str(v) for v in self.insdc_run_accessions]

        if self.library_prep_id is not None and not isinstance(self.library_prep_id, str):
            self.library_prep_id = str(self.library_prep_id)

        super().__post_init__(**kwargs)


@dataclass
class ImageFile(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_FILE.ImageFile
    class_class_curie: ClassVar[str] = "Image_file:ImageFile"
    class_name: ClassVar[str] = "ImageFile"
    class_model_uri: ClassVar[URIRef] = HCA.ImageFile

    describedBy: str = None
    schema_type: Union[str, "ImageFileSchemaTypeOptions"] = None
    file_core: Union[dict, FileCore] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, ImageFileSchemaTypeOptions):
            self.schema_type = ImageFileSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.file_core):
            self.MissingRequiredField("file_core")
        if not isinstance(self.file_core, FileCore):
            self.file_core = FileCore(**as_dict(self.file_core))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        super().__post_init__(**kwargs)


@dataclass
class SupplementaryFile(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SUPPLEMENTARY_FILE.SupplementaryFile
    class_class_curie: ClassVar[str] = "Supplementary_file:SupplementaryFile"
    class_name: ClassVar[str] = "SupplementaryFile"
    class_model_uri: ClassVar[URIRef] = HCA.SupplementaryFile

    describedBy: str = None
    schema_type: Union[str, "SupplementaryFileSchemaTypeOptions"] = None
    file_core: Union[dict, FileCore] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    file_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, SupplementaryFileSchemaTypeOptions):
            self.schema_type = SupplementaryFileSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.file_core):
            self.MissingRequiredField("file_core")
        if not isinstance(self.file_core, FileCore):
            self.file_core = FileCore(**as_dict(self.file_core))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.file_description is not None and not isinstance(self.file_description, str):
            self.file_description = str(self.file_description)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisFile(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_FILE.AnalysisFile
    class_class_curie: ClassVar[str] = "Analysis_file:AnalysisFile"
    class_name: ClassVar[str] = "AnalysisFile"
    class_model_uri: ClassVar[URIRef] = HCA.AnalysisFile

    describedBy: str = None
    schema_type: Union[str, "AnalysisFileSchemaTypeOptions"] = None
    file_core: Union[dict, FileCore] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    matrix_cell_count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, AnalysisFileSchemaTypeOptions):
            self.schema_type = AnalysisFileSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.file_core):
            self.MissingRequiredField("file_core")
        if not isinstance(self.file_core, FileCore):
            self.file_core = FileCore(**as_dict(self.file_core))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.matrix_cell_count is not None and not isinstance(self.matrix_cell_count, int):
            self.matrix_cell_count = int(self.matrix_cell_count)

        super().__post_init__(**kwargs)


@dataclass
class ReferenceFile(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REFERENCE_FILE.ReferenceFile
    class_class_curie: ClassVar[str] = "Reference_file:ReferenceFile"
    class_name: ClassVar[str] = "ReferenceFile"
    class_model_uri: ClassVar[URIRef] = HCA.ReferenceFile

    describedBy: str = None
    schema_type: Union[str, "ReferenceFileSchemaTypeOptions"] = None
    file_core: Union[dict, FileCore] = None
    ncbi_taxon_id: int = None
    genus_species: Union[dict, SpeciesOntology] = None
    reference_type: Union[str, "ReferenceFileReferenceTypeOptions"] = None
    assembly_type: Union[str, "ReferenceFileAssemblyTypeOptions"] = None
    reference_version: str = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, ReferenceFileSchemaTypeOptions):
            self.schema_type = ReferenceFileSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.file_core):
            self.MissingRequiredField("file_core")
        if not isinstance(self.file_core, FileCore):
            self.file_core = FileCore(**as_dict(self.file_core))

        if self._is_empty(self.ncbi_taxon_id):
            self.MissingRequiredField("ncbi_taxon_id")
        if not isinstance(self.ncbi_taxon_id, int):
            self.ncbi_taxon_id = int(self.ncbi_taxon_id)

        if self._is_empty(self.genus_species):
            self.MissingRequiredField("genus_species")
        if not isinstance(self.genus_species, SpeciesOntology):
            self.genus_species = SpeciesOntology(**as_dict(self.genus_species))

        if self._is_empty(self.reference_type):
            self.MissingRequiredField("reference_type")
        if not isinstance(self.reference_type, ReferenceFileReferenceTypeOptions):
            self.reference_type = ReferenceFileReferenceTypeOptions(self.reference_type)

        if self._is_empty(self.assembly_type):
            self.MissingRequiredField("assembly_type")
        if not isinstance(self.assembly_type, ReferenceFileAssemblyTypeOptions):
            self.assembly_type = ReferenceFileAssemblyTypeOptions(self.assembly_type)

        if self._is_empty(self.reference_version):
            self.MissingRequiredField("reference_version")
        if not isinstance(self.reference_version, str):
            self.reference_version = str(self.reference_version)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        super().__post_init__(**kwargs)


@dataclass
class Protocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROTOCOL.Protocol
    class_class_curie: ClassVar[str] = "Protocol:Protocol"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = HCA.Protocol

    describedBy: str = None
    schema_type: Union[str, "ProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    type: Optional[Union[dict, ProcessTypeOntology]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, ProtocolSchemaTypeOptions):
            self.schema_type = ProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.type is not None and not isinstance(self.type, ProcessTypeOntology):
            self.type = ProcessTypeOntology(**as_dict(self.type))

        super().__post_init__(**kwargs)


@dataclass
class SequencingProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEQUENCING_PROTOCOL.SequencingProtocol
    class_class_curie: ClassVar[str] = "Sequencing_protocol:SequencingProtocol"
    class_name: ClassVar[str] = "SequencingProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.SequencingProtocol

    describedBy: str = None
    schema_type: Union[str, "SequencingProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    instrument_manufacturer_model: Union[dict, InstrumentOntology] = None
    paired_end: Union[bool, Bool] = None
    method: Union[dict, SequencingOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    local_machine_name: Optional[str] = None
    s10x: Optional[Union[dict, S10x]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, SequencingProtocolSchemaTypeOptions):
            self.schema_type = SequencingProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.instrument_manufacturer_model):
            self.MissingRequiredField("instrument_manufacturer_model")
        if not isinstance(self.instrument_manufacturer_model, InstrumentOntology):
            self.instrument_manufacturer_model = InstrumentOntology(**as_dict(self.instrument_manufacturer_model))

        if self._is_empty(self.paired_end):
            self.MissingRequiredField("paired_end")
        if not isinstance(self.paired_end, Bool):
            self.paired_end = Bool(self.paired_end)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, SequencingOntology):
            self.method = SequencingOntology(**as_dict(self.method))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.local_machine_name is not None and not isinstance(self.local_machine_name, str):
            self.local_machine_name = str(self.local_machine_name)

        if self.s10x is not None and not isinstance(self.s10x, S10x):
            self.s10x = S10x(**as_dict(self.s10x))

        super().__post_init__(**kwargs)


@dataclass
class LibraryPreparationProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LIBRARY_PREPARATION_PROTOCOL.LibraryPreparationProtocol
    class_class_curie: ClassVar[str] = "Library_preparation_protocol:LibraryPreparationProtocol"
    class_name: ClassVar[str] = "LibraryPreparationProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.LibraryPreparationProtocol

    describedBy: str = None
    schema_type: Union[str, "LibraryPreparationProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    input_nucleic_acid_molecule: Union[dict, BiologicalMacromoleculeOntology] = None
    nucleic_acid_source: Union[str, "LibraryPreparationProtocolNucleicAcidSourceOptions"] = None
    library_construction_method: Union[dict, LibraryConstructionOntology] = None
    end_bias: Union[str, "LibraryPreparationProtocolEndBiasOptions"] = None
    strand: Union[str, "LibraryPreparationProtocolStrandOptions"] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    cell_barcode: Optional[Union[dict, Barcode]] = None
    spatial_barcode: Optional[Union[dict, Barcode]] = None
    library_construction_kit: Optional[Union[dict, PurchasedReagents]] = None
    nucleic_acid_conversion_kit: Optional[Union[dict, PurchasedReagents]] = None
    primer: Optional[Union[str, "LibraryPreparationProtocolPrimerOptions"]] = None
    spike_in_kit: Optional[Union[dict, PurchasedReagents]] = None
    spike_in_dilution: Optional[int] = None
    umi_barcode: Optional[Union[dict, Barcode]] = None
    library_preamplification_method: Optional[Union[dict, LibraryAmplificationOntology]] = None
    cdna_library_amplification_method: Optional[Union[dict, LibraryAmplificationOntology]] = None
    nominal_length: Optional[int] = None
    nominal_sdev: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, LibraryPreparationProtocolSchemaTypeOptions):
            self.schema_type = LibraryPreparationProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.input_nucleic_acid_molecule):
            self.MissingRequiredField("input_nucleic_acid_molecule")
        if not isinstance(self.input_nucleic_acid_molecule, BiologicalMacromoleculeOntology):
            self.input_nucleic_acid_molecule = BiologicalMacromoleculeOntology(**as_dict(self.input_nucleic_acid_molecule))

        if self._is_empty(self.nucleic_acid_source):
            self.MissingRequiredField("nucleic_acid_source")
        if not isinstance(self.nucleic_acid_source, LibraryPreparationProtocolNucleicAcidSourceOptions):
            self.nucleic_acid_source = LibraryPreparationProtocolNucleicAcidSourceOptions(self.nucleic_acid_source)

        if self._is_empty(self.library_construction_method):
            self.MissingRequiredField("library_construction_method")
        if not isinstance(self.library_construction_method, LibraryConstructionOntology):
            self.library_construction_method = LibraryConstructionOntology(**as_dict(self.library_construction_method))

        if self._is_empty(self.end_bias):
            self.MissingRequiredField("end_bias")
        if not isinstance(self.end_bias, LibraryPreparationProtocolEndBiasOptions):
            self.end_bias = LibraryPreparationProtocolEndBiasOptions(self.end_bias)

        if self._is_empty(self.strand):
            self.MissingRequiredField("strand")
        if not isinstance(self.strand, LibraryPreparationProtocolStrandOptions):
            self.strand = LibraryPreparationProtocolStrandOptions(self.strand)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.cell_barcode is not None and not isinstance(self.cell_barcode, Barcode):
            self.cell_barcode = Barcode(**as_dict(self.cell_barcode))

        if self.spatial_barcode is not None and not isinstance(self.spatial_barcode, Barcode):
            self.spatial_barcode = Barcode(**as_dict(self.spatial_barcode))

        if self.library_construction_kit is not None and not isinstance(self.library_construction_kit, PurchasedReagents):
            self.library_construction_kit = PurchasedReagents(**as_dict(self.library_construction_kit))

        if self.nucleic_acid_conversion_kit is not None and not isinstance(self.nucleic_acid_conversion_kit, PurchasedReagents):
            self.nucleic_acid_conversion_kit = PurchasedReagents(**as_dict(self.nucleic_acid_conversion_kit))

        if self.primer is not None and not isinstance(self.primer, LibraryPreparationProtocolPrimerOptions):
            self.primer = LibraryPreparationProtocolPrimerOptions(self.primer)

        if self.spike_in_kit is not None and not isinstance(self.spike_in_kit, PurchasedReagents):
            self.spike_in_kit = PurchasedReagents(**as_dict(self.spike_in_kit))

        if self.spike_in_dilution is not None and not isinstance(self.spike_in_dilution, int):
            self.spike_in_dilution = int(self.spike_in_dilution)

        if self.umi_barcode is not None and not isinstance(self.umi_barcode, Barcode):
            self.umi_barcode = Barcode(**as_dict(self.umi_barcode))

        if self.library_preamplification_method is not None and not isinstance(self.library_preamplification_method, LibraryAmplificationOntology):
            self.library_preamplification_method = LibraryAmplificationOntology(**as_dict(self.library_preamplification_method))

        if self.cdna_library_amplification_method is not None and not isinstance(self.cdna_library_amplification_method, LibraryAmplificationOntology):
            self.cdna_library_amplification_method = LibraryAmplificationOntology(**as_dict(self.cdna_library_amplification_method))

        if self.nominal_length is not None and not isinstance(self.nominal_length, int):
            self.nominal_length = int(self.nominal_length)

        if self.nominal_sdev is not None and not isinstance(self.nominal_sdev, int):
            self.nominal_sdev = int(self.nominal_sdev)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_PROTOCOL.AnalysisProtocol
    class_class_curie: ClassVar[str] = "Analysis_protocol:AnalysisProtocol"
    class_name: ClassVar[str] = "AnalysisProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.AnalysisProtocol

    describedBy: str = None
    schema_type: Union[str, "AnalysisProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    type: Union[dict, ProcessTypeOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    computational_method: Optional[str] = None
    matrix: Optional[Union[dict, Matrix]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, AnalysisProtocolSchemaTypeOptions):
            self.schema_type = AnalysisProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, ProcessTypeOntology):
            self.type = ProcessTypeOntology(**as_dict(self.type))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.computational_method is not None and not isinstance(self.computational_method, str):
            self.computational_method = str(self.computational_method)

        if self.matrix is not None and not isinstance(self.matrix, Matrix):
            self.matrix = Matrix(**as_dict(self.matrix))

        super().__post_init__(**kwargs)


@dataclass
class AggregateGenerationProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AGGREGATE_GENERATION_PROTOCOL.AggregateGenerationProtocol
    class_class_curie: ClassVar[str] = "Aggregate_generation_protocol:AggregateGenerationProtocol"
    class_name: ClassVar[str] = "AggregateGenerationProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.AggregateGenerationProtocol

    describedBy: str = None
    schema_type: Union[str, "AggregateGenerationProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    formation_method: str = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    cell_uniformity: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, AggregateGenerationProtocolSchemaTypeOptions):
            self.schema_type = AggregateGenerationProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.formation_method):
            self.MissingRequiredField("formation_method")
        if not isinstance(self.formation_method, str):
            self.formation_method = str(self.formation_method)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.cell_uniformity is not None and not isinstance(self.cell_uniformity, str):
            self.cell_uniformity = str(self.cell_uniformity)

        super().__post_init__(**kwargs)


@dataclass
class EnrichmentProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ENRICHMENT_PROTOCOL.EnrichmentProtocol
    class_class_curie: ClassVar[str] = "Enrichment_protocol:EnrichmentProtocol"
    class_name: ClassVar[str] = "EnrichmentProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.EnrichmentProtocol

    describedBy: str = None
    schema_type: Union[str, "EnrichmentProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    method: Union[dict, ProcessTypeOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    markers: Optional[str] = None
    minimum_size: Optional[float] = None
    maximum_size: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, EnrichmentProtocolSchemaTypeOptions):
            self.schema_type = EnrichmentProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, ProcessTypeOntology):
            self.method = ProcessTypeOntology(**as_dict(self.method))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.markers is not None and not isinstance(self.markers, str):
            self.markers = str(self.markers)

        if self.minimum_size is not None and not isinstance(self.minimum_size, float):
            self.minimum_size = float(self.minimum_size)

        if self.maximum_size is not None and not isinstance(self.maximum_size, float):
            self.maximum_size = float(self.maximum_size)

        super().__post_init__(**kwargs)


@dataclass
class DissociationProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DISSOCIATION_PROTOCOL.DissociationProtocol
    class_class_curie: ClassVar[str] = "Dissociation_protocol:DissociationProtocol"
    class_name: ClassVar[str] = "DissociationProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.DissociationProtocol

    describedBy: str = None
    schema_type: Union[str, "DissociationProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    method: Union[dict, ProcessTypeOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    reagents: Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, DissociationProtocolSchemaTypeOptions):
            self.schema_type = DissociationProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, ProcessTypeOntology):
            self.method = ProcessTypeOntology(**as_dict(self.method))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if not isinstance(self.reagents, list):
            self.reagents = [self.reagents] if self.reagents is not None else []
        self.reagents = [v if isinstance(v, PurchasedReagents) else PurchasedReagents(**as_dict(v)) for v in self.reagents]

        super().__post_init__(**kwargs)


@dataclass
class IpscInductionProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IPSC_INDUCTION_PROTOCOL.IpscInductionProtocol
    class_class_curie: ClassVar[str] = "iPSC_induction_protocol:IpscInductionProtocol"
    class_name: ClassVar[str] = "IpscInductionProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.IpscInductionProtocol

    describedBy: str = None
    schema_type: Union[str, "IpscInductionProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    method: Union[str, "IpscInductionProtocolMethodOptions"] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    reprogramming_factors: Optional[str] = None
    ipsc_induction_kit: Optional[Union[dict, PurchasedReagents]] = None
    pluripotency_test: Optional[str] = None
    percent_pluripotency: Optional[float] = None
    pluripotency_vector_removed: Optional[Union[str, "IpscInductionProtocolPluripotencyVectorRemovedOptions"]] = None
    reagents: Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, IpscInductionProtocolSchemaTypeOptions):
            self.schema_type = IpscInductionProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, IpscInductionProtocolMethodOptions):
            self.method = IpscInductionProtocolMethodOptions(self.method)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.reprogramming_factors is not None and not isinstance(self.reprogramming_factors, str):
            self.reprogramming_factors = str(self.reprogramming_factors)

        if self.ipsc_induction_kit is not None and not isinstance(self.ipsc_induction_kit, PurchasedReagents):
            self.ipsc_induction_kit = PurchasedReagents(**as_dict(self.ipsc_induction_kit))

        if self.pluripotency_test is not None and not isinstance(self.pluripotency_test, str):
            self.pluripotency_test = str(self.pluripotency_test)

        if self.percent_pluripotency is not None and not isinstance(self.percent_pluripotency, float):
            self.percent_pluripotency = float(self.percent_pluripotency)

        if self.pluripotency_vector_removed is not None and not isinstance(self.pluripotency_vector_removed, IpscInductionProtocolPluripotencyVectorRemovedOptions):
            self.pluripotency_vector_removed = IpscInductionProtocolPluripotencyVectorRemovedOptions(self.pluripotency_vector_removed)

        if not isinstance(self.reagents, list):
            self.reagents = [self.reagents] if self.reagents is not None else []
        self.reagents = [v if isinstance(v, PurchasedReagents) else PurchasedReagents(**as_dict(v)) for v in self.reagents]

        super().__post_init__(**kwargs)


@dataclass
class CollectionProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTION_PROTOCOL.CollectionProtocol
    class_class_curie: ClassVar[str] = "Collection_protocol:CollectionProtocol"
    class_name: ClassVar[str] = "CollectionProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.CollectionProtocol

    describedBy: str = None
    schema_type: Union[str, "CollectionProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    method: Union[dict, ProcessTypeOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    reagents: Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, CollectionProtocolSchemaTypeOptions):
            self.schema_type = CollectionProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, ProcessTypeOntology):
            self.method = ProcessTypeOntology(**as_dict(self.method))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if not isinstance(self.reagents, list):
            self.reagents = [self.reagents] if self.reagents is not None else []
        self.reagents = [v if isinstance(v, PurchasedReagents) else PurchasedReagents(**as_dict(v)) for v in self.reagents]

        super().__post_init__(**kwargs)


@dataclass
class DifferentiationProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIFFERENTIATION_PROTOCOL.DifferentiationProtocol
    class_class_curie: ClassVar[str] = "Differentiation_protocol:DifferentiationProtocol"
    class_name: ClassVar[str] = "DifferentiationProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.DifferentiationProtocol

    describedBy: str = None
    schema_type: Union[str, "DifferentiationProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    method: str = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    media: Optional[str] = None
    small_molecules: Optional[str] = None
    target_cell_yield: Optional[float] = None
    reagents: Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]] = empty_list()
    target_pathway: Optional[str] = None
    validation_method: Optional[str] = None
    validation_result: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, DifferentiationProtocolSchemaTypeOptions):
            self.schema_type = DifferentiationProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.media is not None and not isinstance(self.media, str):
            self.media = str(self.media)

        if self.small_molecules is not None and not isinstance(self.small_molecules, str):
            self.small_molecules = str(self.small_molecules)

        if self.target_cell_yield is not None and not isinstance(self.target_cell_yield, float):
            self.target_cell_yield = float(self.target_cell_yield)

        if not isinstance(self.reagents, list):
            self.reagents = [self.reagents] if self.reagents is not None else []
        self.reagents = [v if isinstance(v, PurchasedReagents) else PurchasedReagents(**as_dict(v)) for v in self.reagents]

        if self.target_pathway is not None and not isinstance(self.target_pathway, str):
            self.target_pathway = str(self.target_pathway)

        if self.validation_method is not None and not isinstance(self.validation_method, str):
            self.validation_method = str(self.validation_method)

        if self.validation_result is not None and not isinstance(self.validation_result, str):
            self.validation_result = str(self.validation_result)

        super().__post_init__(**kwargs)


@dataclass
class TreatmentProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TREATMENT_PROTOCOL.TreatmentProtocol
    class_class_curie: ClassVar[str] = "Treatment_protocol:TreatmentProtocol"
    class_name: ClassVar[str] = "TreatmentProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.TreatmentProtocol

    describedBy: str = None
    schema_type: Union[str, "TreatmentProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    method: Union[Union[dict, TreatmentMethodOntology], List[Union[dict, TreatmentMethodOntology]]] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    media: Optional[str] = None
    reagents: Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]] = empty_list()
    target_pathway: Optional[Union[Union[dict, TargetPathwayOntology], List[Union[dict, TargetPathwayOntology]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, TreatmentProtocolSchemaTypeOptions):
            self.schema_type = TreatmentProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        self._normalize_inlined_as_dict(slot_name="method", slot_type=TreatmentMethodOntology, key_name="text", keyed=False)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.media is not None and not isinstance(self.media, str):
            self.media = str(self.media)

        if not isinstance(self.reagents, list):
            self.reagents = [self.reagents] if self.reagents is not None else []
        self.reagents = [v if isinstance(v, PurchasedReagents) else PurchasedReagents(**as_dict(v)) for v in self.reagents]

        self._normalize_inlined_as_dict(slot_name="target_pathway", slot_type=TargetPathwayOntology, key_name="text", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ImagingPreparationProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGING_PREPARATION_PROTOCOL.ImagingPreparationProtocol
    class_class_curie: ClassVar[str] = "Imaging_preparation_protocol:ImagingPreparationProtocol"
    class_name: ClassVar[str] = "ImagingPreparationProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.ImagingPreparationProtocol

    describedBy: str = None
    schema_type: Union[str, "ImagingPreparationProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    fresh_slicing_method: Optional[str] = None
    imaged_slice_thickness: Optional[float] = None
    final_slicing_method: Optional[str] = None
    post_resection_interval: Optional[float] = None
    post_resection_interval_unit: Optional[Union[dict, TimeUnitOntology]] = None
    pre_final_slice_preservation_method: Optional[Union[dict, PreservationStorage]] = None
    post_final_slicing_interval: Optional[float] = None
    post_final_slicing_interval_unit: Optional[Union[dict, TimeUnitOntology]] = None
    fiducial_marker: Optional[str] = None
    expansion_factor: Optional[float] = None
    permeabilisation_time: Optional[float] = None
    permeabilisation_time_unit: Optional[Union[dict, TimeUnitOntology]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, ImagingPreparationProtocolSchemaTypeOptions):
            self.schema_type = ImagingPreparationProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.fresh_slicing_method is not None and not isinstance(self.fresh_slicing_method, str):
            self.fresh_slicing_method = str(self.fresh_slicing_method)

        if self.imaged_slice_thickness is not None and not isinstance(self.imaged_slice_thickness, float):
            self.imaged_slice_thickness = float(self.imaged_slice_thickness)

        if self.final_slicing_method is not None and not isinstance(self.final_slicing_method, str):
            self.final_slicing_method = str(self.final_slicing_method)

        if self.post_resection_interval is not None and not isinstance(self.post_resection_interval, float):
            self.post_resection_interval = float(self.post_resection_interval)

        if self.post_resection_interval_unit is not None and not isinstance(self.post_resection_interval_unit, TimeUnitOntology):
            self.post_resection_interval_unit = TimeUnitOntology(**as_dict(self.post_resection_interval_unit))

        if self.pre_final_slice_preservation_method is not None and not isinstance(self.pre_final_slice_preservation_method, PreservationStorage):
            self.pre_final_slice_preservation_method = PreservationStorage(**as_dict(self.pre_final_slice_preservation_method))

        if self.post_final_slicing_interval is not None and not isinstance(self.post_final_slicing_interval, float):
            self.post_final_slicing_interval = float(self.post_final_slicing_interval)

        if self.post_final_slicing_interval_unit is not None and not isinstance(self.post_final_slicing_interval_unit, TimeUnitOntology):
            self.post_final_slicing_interval_unit = TimeUnitOntology(**as_dict(self.post_final_slicing_interval_unit))

        if self.fiducial_marker is not None and not isinstance(self.fiducial_marker, str):
            self.fiducial_marker = str(self.fiducial_marker)

        if self.expansion_factor is not None and not isinstance(self.expansion_factor, float):
            self.expansion_factor = float(self.expansion_factor)

        if self.permeabilisation_time is not None and not isinstance(self.permeabilisation_time, float):
            self.permeabilisation_time = float(self.permeabilisation_time)

        if self.permeabilisation_time_unit is not None and not isinstance(self.permeabilisation_time_unit, TimeUnitOntology):
            self.permeabilisation_time_unit = TimeUnitOntology(**as_dict(self.permeabilisation_time_unit))

        super().__post_init__(**kwargs)


@dataclass
class ImagingProtocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGING_PROTOCOL.ImagingProtocol
    class_class_curie: ClassVar[str] = "Imaging_Protocol:ImagingProtocol"
    class_name: ClassVar[str] = "ImagingProtocol"
    class_model_uri: ClassVar[URIRef] = HCA.ImagingProtocol

    describedBy: str = None
    schema_type: Union[str, "ImagingProtocolSchemaTypeOptions"] = None
    protocol_core: Union[dict, ProtocolCore] = None
    microscopy_technique: Union[dict, MicroscopyOntology] = None
    magnification: str = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    microscope_setup_description: Optional[str] = None
    numerical_aperture: Optional[float] = None
    immersion_medium_type: Optional[str] = None
    immersion_medium_refractive_index: Optional[float] = None
    pixel_size: Optional[float] = None
    number_of_tiles: Optional[int] = None
    tile_size_y: Optional[float] = None
    tile_size_x: Optional[float] = None
    z_stack_step_size: Optional[float] = None
    number_of_z_steps: Optional[int] = None
    overlapping_tiles: Optional[Union[str, "ImagingProtocolOverlappingTilesOptions"]] = None
    channel: Optional[Union[Union[dict, Channel], List[Union[dict, Channel]]]] = empty_list()
    probe: Optional[Union[Union[dict, Probe], List[Union[dict, Probe]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, ImagingProtocolSchemaTypeOptions):
            self.schema_type = ImagingProtocolSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.protocol_core):
            self.MissingRequiredField("protocol_core")
        if not isinstance(self.protocol_core, ProtocolCore):
            self.protocol_core = ProtocolCore(**as_dict(self.protocol_core))

        if self._is_empty(self.microscopy_technique):
            self.MissingRequiredField("microscopy_technique")
        if not isinstance(self.microscopy_technique, MicroscopyOntology):
            self.microscopy_technique = MicroscopyOntology(**as_dict(self.microscopy_technique))

        if self._is_empty(self.magnification):
            self.MissingRequiredField("magnification")
        if not isinstance(self.magnification, str):
            self.magnification = str(self.magnification)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.microscope_setup_description is not None and not isinstance(self.microscope_setup_description, str):
            self.microscope_setup_description = str(self.microscope_setup_description)

        if self.numerical_aperture is not None and not isinstance(self.numerical_aperture, float):
            self.numerical_aperture = float(self.numerical_aperture)

        if self.immersion_medium_type is not None and not isinstance(self.immersion_medium_type, str):
            self.immersion_medium_type = str(self.immersion_medium_type)

        if self.immersion_medium_refractive_index is not None and not isinstance(self.immersion_medium_refractive_index, float):
            self.immersion_medium_refractive_index = float(self.immersion_medium_refractive_index)

        if self.pixel_size is not None and not isinstance(self.pixel_size, float):
            self.pixel_size = float(self.pixel_size)

        if self.number_of_tiles is not None and not isinstance(self.number_of_tiles, int):
            self.number_of_tiles = int(self.number_of_tiles)

        if self.tile_size_y is not None and not isinstance(self.tile_size_y, float):
            self.tile_size_y = float(self.tile_size_y)

        if self.tile_size_x is not None and not isinstance(self.tile_size_x, float):
            self.tile_size_x = float(self.tile_size_x)

        if self.z_stack_step_size is not None and not isinstance(self.z_stack_step_size, float):
            self.z_stack_step_size = float(self.z_stack_step_size)

        if self.number_of_z_steps is not None and not isinstance(self.number_of_z_steps, int):
            self.number_of_z_steps = int(self.number_of_z_steps)

        if self.overlapping_tiles is not None and not isinstance(self.overlapping_tiles, ImagingProtocolOverlappingTilesOptions):
            self.overlapping_tiles = ImagingProtocolOverlappingTilesOptions(self.overlapping_tiles)

        self._normalize_inlined_as_dict(slot_name="channel", slot_type=Channel, key_name="channel_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="probe", slot_type=Probe, key_name="probe_label", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Project(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROJECT.Project
    class_class_curie: ClassVar[str] = "Project:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = HCA.Project

    describedBy: str = None
    schema_type: Union[str, "ProjectSchemaTypeOptions"] = None
    project_core: Union[dict, ProjectCore] = None
    funders: Union[Union[dict, Funder], List[Union[dict, Funder]]] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    contributors: Optional[Union[Union[dict, Contact], List[Union[dict, Contact]]]] = empty_list()
    supplementary_links: Optional[Union[str, List[str]]] = empty_list()
    publications: Optional[Union[Union[dict, Publication], List[Union[dict, Publication]]]] = empty_list()
    insdc_project_accessions: Optional[Union[str, List[str]]] = empty_list()
    ega_accessions: Optional[Union[str, List[str]]] = empty_list()
    dbgap_accessions: Optional[Union[str, List[str]]] = empty_list()
    geo_series_accessions: Optional[Union[str, List[str]]] = empty_list()
    array_express_accessions: Optional[Union[str, List[str]]] = empty_list()
    insdc_study_accessions: Optional[Union[str, List[str]]] = empty_list()
    biostudies_accessions: Optional[Union[str, List[str]]] = empty_list()
    estimated_cell_count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, ProjectSchemaTypeOptions):
            self.schema_type = ProjectSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.project_core):
            self.MissingRequiredField("project_core")
        if not isinstance(self.project_core, ProjectCore):
            self.project_core = ProjectCore(**as_dict(self.project_core))

        if self._is_empty(self.funders):
            self.MissingRequiredField("funders")
        self._normalize_inlined_as_dict(slot_name="funders", slot_type=Funder, key_name="grant_id", keyed=False)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        self._normalize_inlined_as_dict(slot_name="contributors", slot_type=Contact, key_name="institution", keyed=False)

        if not isinstance(self.supplementary_links, list):
            self.supplementary_links = [self.supplementary_links] if self.supplementary_links is not None else []
        self.supplementary_links = [v if isinstance(v, str) else str(v) for v in self.supplementary_links]

        self._normalize_inlined_as_dict(slot_name="publications", slot_type=Publication, key_name="authors", keyed=False)

        if not isinstance(self.insdc_project_accessions, list):
            self.insdc_project_accessions = [self.insdc_project_accessions] if self.insdc_project_accessions is not None else []
        self.insdc_project_accessions = [v if isinstance(v, str) else str(v) for v in self.insdc_project_accessions]

        if not isinstance(self.ega_accessions, list):
            self.ega_accessions = [self.ega_accessions] if self.ega_accessions is not None else []
        self.ega_accessions = [v if isinstance(v, str) else str(v) for v in self.ega_accessions]

        if not isinstance(self.dbgap_accessions, list):
            self.dbgap_accessions = [self.dbgap_accessions] if self.dbgap_accessions is not None else []
        self.dbgap_accessions = [v if isinstance(v, str) else str(v) for v in self.dbgap_accessions]

        if not isinstance(self.geo_series_accessions, list):
            self.geo_series_accessions = [self.geo_series_accessions] if self.geo_series_accessions is not None else []
        self.geo_series_accessions = [v if isinstance(v, str) else str(v) for v in self.geo_series_accessions]

        if not isinstance(self.array_express_accessions, list):
            self.array_express_accessions = [self.array_express_accessions] if self.array_express_accessions is not None else []
        self.array_express_accessions = [v if isinstance(v, str) else str(v) for v in self.array_express_accessions]

        if not isinstance(self.insdc_study_accessions, list):
            self.insdc_study_accessions = [self.insdc_study_accessions] if self.insdc_study_accessions is not None else []
        self.insdc_study_accessions = [v if isinstance(v, str) else str(v) for v in self.insdc_study_accessions]

        if not isinstance(self.biostudies_accessions, list):
            self.biostudies_accessions = [self.biostudies_accessions] if self.biostudies_accessions is not None else []
        self.biostudies_accessions = [v if isinstance(v, str) else str(v) for v in self.biostudies_accessions]

        if self.estimated_cell_count is not None and not isinstance(self.estimated_cell_count, int):
            self.estimated_cell_count = int(self.estimated_cell_count)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenFromOrganism(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPECIMEN_FROM_ORGANISM.SpecimenFromOrganism
    class_class_curie: ClassVar[str] = "Specimen_from_organism:SpecimenFromOrganism"
    class_name: ClassVar[str] = "SpecimenFromOrganism"
    class_model_uri: ClassVar[URIRef] = HCA.SpecimenFromOrganism

    describedBy: str = None
    schema_type: Union[str, "SpecimenFromOrganismSchemaTypeOptions"] = None
    biomaterial_core: Union[dict, BiomaterialCore] = None
    organ: Union[dict, OrganOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    genus_species: Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]] = empty_list()
    organ_parts: Optional[Union[Union[dict, OrganPartOntology], List[Union[dict, OrganPartOntology]]]] = empty_list()
    diseases: Optional[Union[Union[dict, DiseaseOntology], List[Union[dict, DiseaseOntology]]]] = empty_list()
    state_of_specimen: Optional[Union[dict, StateOfSpecimen]] = None
    preservation_storage: Optional[Union[dict, PreservationStorage]] = None
    collection_time: Optional[str] = None
    purchased_specimen: Optional[Union[dict, PurchasedReagents]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, SpecimenFromOrganismSchemaTypeOptions):
            self.schema_type = SpecimenFromOrganismSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.biomaterial_core):
            self.MissingRequiredField("biomaterial_core")
        if not isinstance(self.biomaterial_core, BiomaterialCore):
            self.biomaterial_core = BiomaterialCore(**as_dict(self.biomaterial_core))

        if self._is_empty(self.organ):
            self.MissingRequiredField("organ")
        if not isinstance(self.organ, OrganOntology):
            self.organ = OrganOntology(**as_dict(self.organ))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        self._normalize_inlined_as_dict(slot_name="genus_species", slot_type=SpeciesOntology, key_name="text", keyed=False)

        self._normalize_inlined_as_dict(slot_name="organ_parts", slot_type=OrganPartOntology, key_name="text", keyed=False)

        self._normalize_inlined_as_dict(slot_name="diseases", slot_type=DiseaseOntology, key_name="text", keyed=False)

        if self.state_of_specimen is not None and not isinstance(self.state_of_specimen, StateOfSpecimen):
            self.state_of_specimen = StateOfSpecimen(**as_dict(self.state_of_specimen))

        if self.preservation_storage is not None and not isinstance(self.preservation_storage, PreservationStorage):
            self.preservation_storage = PreservationStorage(**as_dict(self.preservation_storage))

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.purchased_specimen is not None and not isinstance(self.purchased_specimen, PurchasedReagents):
            self.purchased_specimen = PurchasedReagents(**as_dict(self.purchased_specimen))

        super().__post_init__(**kwargs)


@dataclass
class CellSuspension(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELL_SUSPENSION.CellSuspension
    class_class_curie: ClassVar[str] = "Cell_suspension:CellSuspension"
    class_name: ClassVar[str] = "CellSuspension"
    class_model_uri: ClassVar[URIRef] = HCA.CellSuspension

    describedBy: str = None
    schema_type: Union[str, "CellSuspensionSchemaTypeOptions"] = None
    biomaterial_core: Union[dict, BiomaterialCore] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    cell_morphology: Optional[Union[dict, CellMorphology]] = None
    growth_conditions: Optional[Union[dict, GrowthConditions]] = None
    genus_species: Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]] = empty_list()
    selected_cell_types: Optional[Union[Union[dict, CellTypeOntology], List[Union[dict, CellTypeOntology]]]] = empty_list()
    estimated_cell_count: Optional[int] = None
    plate_based_sequencing: Optional[Union[dict, PlateBasedSequencing]] = None
    timecourse: Optional[Union[dict, Timecourse]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, CellSuspensionSchemaTypeOptions):
            self.schema_type = CellSuspensionSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.biomaterial_core):
            self.MissingRequiredField("biomaterial_core")
        if not isinstance(self.biomaterial_core, BiomaterialCore):
            self.biomaterial_core = BiomaterialCore(**as_dict(self.biomaterial_core))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.cell_morphology is not None and not isinstance(self.cell_morphology, CellMorphology):
            self.cell_morphology = CellMorphology(**as_dict(self.cell_morphology))

        if self.growth_conditions is not None and not isinstance(self.growth_conditions, GrowthConditions):
            self.growth_conditions = GrowthConditions(**as_dict(self.growth_conditions))

        self._normalize_inlined_as_dict(slot_name="genus_species", slot_type=SpeciesOntology, key_name="text", keyed=False)

        self._normalize_inlined_as_dict(slot_name="selected_cell_types", slot_type=CellTypeOntology, key_name="text", keyed=False)

        if self.estimated_cell_count is not None and not isinstance(self.estimated_cell_count, int):
            self.estimated_cell_count = int(self.estimated_cell_count)

        if self.plate_based_sequencing is not None and not isinstance(self.plate_based_sequencing, PlateBasedSequencing):
            self.plate_based_sequencing = PlateBasedSequencing(**as_dict(self.plate_based_sequencing))

        if self.timecourse is not None and not isinstance(self.timecourse, Timecourse):
            self.timecourse = Timecourse(**as_dict(self.timecourse))

        super().__post_init__(**kwargs)


@dataclass
class CellLine(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELL_LINE.CellLine
    class_class_curie: ClassVar[str] = "Cell_line:CellLine"
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = HCA.CellLine

    describedBy: str = None
    schema_type: Union[str, "CellLineSchemaTypeOptions"] = None
    biomaterial_core: Union[dict, BiomaterialCore] = None
    type: Union[str, "CellLineTypeOptions"] = None
    model_organ: Union[dict, OrganOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    supplier: Optional[str] = None
    catalog_number: Optional[str] = None
    lot_number: Optional[str] = None
    catalog_url: Optional[str] = None
    cell_cycle: Optional[Union[dict, CellCycleOntology]] = None
    cell_morphology: Optional[Union[dict, CellMorphology]] = None
    growth_conditions: Optional[Union[dict, GrowthConditions]] = None
    confluency: Optional[float] = None
    cell_type: Optional[Union[dict, CellTypeOntology]] = None
    karyotype: Optional[str] = None
    tissue: Optional[Union[dict, OrganPartOntology]] = None
    date_established: Optional[str] = None
    disease: Optional[Union[dict, DiseaseOntology]] = None
    genus_species: Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]] = empty_list()
    publication: Optional[Union[dict, Publication]] = None
    timecourse: Optional[Union[dict, Timecourse]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, CellLineSchemaTypeOptions):
            self.schema_type = CellLineSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.biomaterial_core):
            self.MissingRequiredField("biomaterial_core")
        if not isinstance(self.biomaterial_core, BiomaterialCore):
            self.biomaterial_core = BiomaterialCore(**as_dict(self.biomaterial_core))

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, CellLineTypeOptions):
            self.type = CellLineTypeOptions(self.type)

        if self._is_empty(self.model_organ):
            self.MissingRequiredField("model_organ")
        if not isinstance(self.model_organ, OrganOntology):
            self.model_organ = OrganOntology(**as_dict(self.model_organ))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.supplier is not None and not isinstance(self.supplier, str):
            self.supplier = str(self.supplier)

        if self.catalog_number is not None and not isinstance(self.catalog_number, str):
            self.catalog_number = str(self.catalog_number)

        if self.lot_number is not None and not isinstance(self.lot_number, str):
            self.lot_number = str(self.lot_number)

        if self.catalog_url is not None and not isinstance(self.catalog_url, str):
            self.catalog_url = str(self.catalog_url)

        if self.cell_cycle is not None and not isinstance(self.cell_cycle, CellCycleOntology):
            self.cell_cycle = CellCycleOntology(**as_dict(self.cell_cycle))

        if self.cell_morphology is not None and not isinstance(self.cell_morphology, CellMorphology):
            self.cell_morphology = CellMorphology(**as_dict(self.cell_morphology))

        if self.growth_conditions is not None and not isinstance(self.growth_conditions, GrowthConditions):
            self.growth_conditions = GrowthConditions(**as_dict(self.growth_conditions))

        if self.confluency is not None and not isinstance(self.confluency, float):
            self.confluency = float(self.confluency)

        if self.cell_type is not None and not isinstance(self.cell_type, CellTypeOntology):
            self.cell_type = CellTypeOntology(**as_dict(self.cell_type))

        if self.karyotype is not None and not isinstance(self.karyotype, str):
            self.karyotype = str(self.karyotype)

        if self.tissue is not None and not isinstance(self.tissue, OrganPartOntology):
            self.tissue = OrganPartOntology(**as_dict(self.tissue))

        if self.date_established is not None and not isinstance(self.date_established, str):
            self.date_established = str(self.date_established)

        if self.disease is not None and not isinstance(self.disease, DiseaseOntology):
            self.disease = DiseaseOntology(**as_dict(self.disease))

        self._normalize_inlined_as_dict(slot_name="genus_species", slot_type=SpeciesOntology, key_name="text", keyed=False)

        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        if self.timecourse is not None and not isinstance(self.timecourse, Timecourse):
            self.timecourse = Timecourse(**as_dict(self.timecourse))

        super().__post_init__(**kwargs)


@dataclass
class ImagedSpecimen(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGED_SPECIMEN.ImagedSpecimen
    class_class_curie: ClassVar[str] = "Imaged_specimen:ImagedSpecimen"
    class_name: ClassVar[str] = "ImagedSpecimen"
    class_model_uri: ClassVar[URIRef] = HCA.ImagedSpecimen

    describedBy: str = None
    schema_type: Union[str, "ImagedSpecimenSchemaTypeOptions"] = None
    biomaterial_core: Union[dict, BiomaterialCore] = None
    slice_thickness: float = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    overview_images: Optional[Union[str, List[str]]] = empty_list()
    internal_anatomical_structures: Optional[Union[Union[dict, OrganPartOntology], List[Union[dict, OrganPartOntology]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, ImagedSpecimenSchemaTypeOptions):
            self.schema_type = ImagedSpecimenSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.biomaterial_core):
            self.MissingRequiredField("biomaterial_core")
        if not isinstance(self.biomaterial_core, BiomaterialCore):
            self.biomaterial_core = BiomaterialCore(**as_dict(self.biomaterial_core))

        if self._is_empty(self.slice_thickness):
            self.MissingRequiredField("slice_thickness")
        if not isinstance(self.slice_thickness, float):
            self.slice_thickness = float(self.slice_thickness)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if not isinstance(self.overview_images, list):
            self.overview_images = [self.overview_images] if self.overview_images is not None else []
        self.overview_images = [v if isinstance(v, str) else str(v) for v in self.overview_images]

        self._normalize_inlined_as_dict(slot_name="internal_anatomical_structures", slot_type=OrganPartOntology, key_name="text", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DonorOrganism(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DONOR_ORGANISM.DonorOrganism
    class_class_curie: ClassVar[str] = "Donor_organism:DonorOrganism"
    class_name: ClassVar[str] = "DonorOrganism"
    class_model_uri: ClassVar[URIRef] = HCA.DonorOrganism

    describedBy: str = None
    schema_type: Union[str, "DonorOrganismSchemaTypeOptions"] = None
    biomaterial_core: Union[dict, BiomaterialCore] = None
    sex: Union[str, "DonorOrganismSexOptions"] = None
    is_living: Union[str, "DonorOrganismIsLivingOptions"] = None
    development_stage: Union[dict, DevelopmentStageOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    human_specific: Optional[Union[dict, HumanSpecific]] = None
    mouse_specific: Optional[Union[dict, MouseSpecific]] = None
    genus_species: Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]] = empty_list()
    organism_age: Optional[str] = None
    organism_age_unit: Optional[Union[dict, TimeUnitOntology]] = None
    diseases: Optional[Union[Union[dict, DiseaseOntology], List[Union[dict, DiseaseOntology]]]] = empty_list()
    death: Optional[Union[dict, Death]] = None
    familial_relationships: Optional[Union[Union[dict, FamilialRelationship], List[Union[dict, FamilialRelationship]]]] = empty_list()
    medical_history: Optional[Union[dict, MedicalHistory]] = None
    gestational_age: Optional[str] = None
    gestational_age_unit: Optional[Union[dict, TimeUnitOntology]] = None
    height: Optional[str] = None
    height_unit: Optional[Union[dict, LengthUnitOntology]] = None
    weight: Optional[str] = None
    weight_unit: Optional[Union[dict, MassUnitOntology]] = None
    timecourse: Optional[Union[dict, Timecourse]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, DonorOrganismSchemaTypeOptions):
            self.schema_type = DonorOrganismSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.biomaterial_core):
            self.MissingRequiredField("biomaterial_core")
        if not isinstance(self.biomaterial_core, BiomaterialCore):
            self.biomaterial_core = BiomaterialCore(**as_dict(self.biomaterial_core))

        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, DonorOrganismSexOptions):
            self.sex = DonorOrganismSexOptions(self.sex)

        if self._is_empty(self.is_living):
            self.MissingRequiredField("is_living")
        if not isinstance(self.is_living, DonorOrganismIsLivingOptions):
            self.is_living = DonorOrganismIsLivingOptions(self.is_living)

        if self._is_empty(self.development_stage):
            self.MissingRequiredField("development_stage")
        if not isinstance(self.development_stage, DevelopmentStageOntology):
            self.development_stage = DevelopmentStageOntology(**as_dict(self.development_stage))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.human_specific is not None and not isinstance(self.human_specific, HumanSpecific):
            self.human_specific = HumanSpecific(**as_dict(self.human_specific))

        if self.mouse_specific is not None and not isinstance(self.mouse_specific, MouseSpecific):
            self.mouse_specific = MouseSpecific(**as_dict(self.mouse_specific))

        self._normalize_inlined_as_dict(slot_name="genus_species", slot_type=SpeciesOntology, key_name="text", keyed=False)

        if self.organism_age is not None and not isinstance(self.organism_age, str):
            self.organism_age = str(self.organism_age)

        if self.organism_age_unit is not None and not isinstance(self.organism_age_unit, TimeUnitOntology):
            self.organism_age_unit = TimeUnitOntology(**as_dict(self.organism_age_unit))

        self._normalize_inlined_as_dict(slot_name="diseases", slot_type=DiseaseOntology, key_name="text", keyed=False)

        if self.death is not None and not isinstance(self.death, Death):
            self.death = Death(**as_dict(self.death))

        if not isinstance(self.familial_relationships, list):
            self.familial_relationships = [self.familial_relationships] if self.familial_relationships is not None else []
        self.familial_relationships = [v if isinstance(v, FamilialRelationship) else FamilialRelationship(**as_dict(v)) for v in self.familial_relationships]

        if self.medical_history is not None and not isinstance(self.medical_history, MedicalHistory):
            self.medical_history = MedicalHistory(**as_dict(self.medical_history))

        if self.gestational_age is not None and not isinstance(self.gestational_age, str):
            self.gestational_age = str(self.gestational_age)

        if self.gestational_age_unit is not None and not isinstance(self.gestational_age_unit, TimeUnitOntology):
            self.gestational_age_unit = TimeUnitOntology(**as_dict(self.gestational_age_unit))

        if self.height is not None and not isinstance(self.height, str):
            self.height = str(self.height)

        if self.height_unit is not None and not isinstance(self.height_unit, LengthUnitOntology):
            self.height_unit = LengthUnitOntology(**as_dict(self.height_unit))

        if self.weight is not None and not isinstance(self.weight, str):
            self.weight = str(self.weight)

        if self.weight_unit is not None and not isinstance(self.weight_unit, MassUnitOntology):
            self.weight_unit = MassUnitOntology(**as_dict(self.weight_unit))

        if self.timecourse is not None and not isinstance(self.timecourse, Timecourse):
            self.timecourse = Timecourse(**as_dict(self.timecourse))

        super().__post_init__(**kwargs)


@dataclass
class Organoid(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANOID.Organoid
    class_class_curie: ClassVar[str] = "Organoid:Organoid"
    class_name: ClassVar[str] = "Organoid"
    class_model_uri: ClassVar[URIRef] = HCA.Organoid

    describedBy: str = None
    schema_type: Union[str, "OrganoidSchemaTypeOptions"] = None
    biomaterial_core: Union[dict, BiomaterialCore] = None
    model_organ: Union[dict, OrganOntology] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    genus_species: Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]] = empty_list()
    model_organ_part: Optional[Union[dict, OrganPartOntology]] = None
    age: Optional[float] = None
    age_unit: Optional[Union[dict, TimeUnitOntology]] = None
    size: Optional[float] = None
    size_unit: Optional[Union[dict, LengthUnitOntology]] = None
    morphology: Optional[str] = None
    embedded_in_matrigel: Optional[Union[bool, Bool]] = None
    growth_environment: Optional[str] = None
    input_aggregate_cell_count: Optional[float] = None
    stored_oxygen_levels: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, OrganoidSchemaTypeOptions):
            self.schema_type = OrganoidSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.biomaterial_core):
            self.MissingRequiredField("biomaterial_core")
        if not isinstance(self.biomaterial_core, BiomaterialCore):
            self.biomaterial_core = BiomaterialCore(**as_dict(self.biomaterial_core))

        if self._is_empty(self.model_organ):
            self.MissingRequiredField("model_organ")
        if not isinstance(self.model_organ, OrganOntology):
            self.model_organ = OrganOntology(**as_dict(self.model_organ))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        self._normalize_inlined_as_dict(slot_name="genus_species", slot_type=SpeciesOntology, key_name="text", keyed=False)

        if self.model_organ_part is not None and not isinstance(self.model_organ_part, OrganPartOntology):
            self.model_organ_part = OrganPartOntology(**as_dict(self.model_organ_part))

        if self.age is not None and not isinstance(self.age, float):
            self.age = float(self.age)

        if self.age_unit is not None and not isinstance(self.age_unit, TimeUnitOntology):
            self.age_unit = TimeUnitOntology(**as_dict(self.age_unit))

        if self.size is not None and not isinstance(self.size, float):
            self.size = float(self.size)

        if self.size_unit is not None and not isinstance(self.size_unit, LengthUnitOntology):
            self.size_unit = LengthUnitOntology(**as_dict(self.size_unit))

        if self.morphology is not None and not isinstance(self.morphology, str):
            self.morphology = str(self.morphology)

        if self.embedded_in_matrigel is not None and not isinstance(self.embedded_in_matrigel, Bool):
            self.embedded_in_matrigel = Bool(self.embedded_in_matrigel)

        if self.growth_environment is not None and not isinstance(self.growth_environment, str):
            self.growth_environment = str(self.growth_environment)

        if self.input_aggregate_cell_count is not None and not isinstance(self.input_aggregate_cell_count, float):
            self.input_aggregate_cell_count = float(self.input_aggregate_cell_count)

        if self.stored_oxygen_levels is not None and not isinstance(self.stored_oxygen_levels, float):
            self.stored_oxygen_levels = float(self.stored_oxygen_levels)

        super().__post_init__(**kwargs)


@dataclass
class Process(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROCESS.Process
    class_class_curie: ClassVar[str] = "Process:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = HCA.Process

    describedBy: str = None
    schema_type: Union[str, "ProcessSchemaTypeOptions"] = None
    process_core: Union[dict, ProcessCore] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    length_of_time: Optional[str] = None
    length_of_time_unit: Optional[Union[dict, TimeUnitOntology]] = None
    type: Optional[Union[dict, ProcessTypeOntology]] = None
    deviation_from_protocol: Optional[str] = None
    insdc_experiment: Optional[Union[dict, InsdcExperiment]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, ProcessSchemaTypeOptions):
            self.schema_type = ProcessSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.process_core):
            self.MissingRequiredField("process_core")
        if not isinstance(self.process_core, ProcessCore):
            self.process_core = ProcessCore(**as_dict(self.process_core))

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.start_time is not None and not isinstance(self.start_time, str):
            self.start_time = str(self.start_time)

        if self.end_time is not None and not isinstance(self.end_time, str):
            self.end_time = str(self.end_time)

        if self.length_of_time is not None and not isinstance(self.length_of_time, str):
            self.length_of_time = str(self.length_of_time)

        if self.length_of_time_unit is not None and not isinstance(self.length_of_time_unit, TimeUnitOntology):
            self.length_of_time_unit = TimeUnitOntology(**as_dict(self.length_of_time_unit))

        if self.type is not None and not isinstance(self.type, ProcessTypeOntology):
            self.type = ProcessTypeOntology(**as_dict(self.type))

        if self.deviation_from_protocol is not None and not isinstance(self.deviation_from_protocol, str):
            self.deviation_from_protocol = str(self.deviation_from_protocol)

        if self.insdc_experiment is not None and not isinstance(self.insdc_experiment, InsdcExperiment):
            self.insdc_experiment = InsdcExperiment(**as_dict(self.insdc_experiment))

        super().__post_init__(**kwargs)


@dataclass
class Task(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_PROCESS.Task
    class_class_curie: ClassVar[str] = "Analysis_process:Task"
    class_name: ClassVar[str] = "Task"
    class_model_uri: ClassVar[URIRef] = HCA.Task

    disk_size: str = None
    task_name: str = None
    zone: str = None
    start_time: str = None
    cpus: int = None
    stop_time: str = None
    memory: str = None
    docker_image: str = None
    log_err: Optional[str] = None
    log_out: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.disk_size):
            self.MissingRequiredField("disk_size")
        if not isinstance(self.disk_size, str):
            self.disk_size = str(self.disk_size)

        if self._is_empty(self.task_name):
            self.MissingRequiredField("task_name")
        if not isinstance(self.task_name, str):
            self.task_name = str(self.task_name)

        if self._is_empty(self.zone):
            self.MissingRequiredField("zone")
        if not isinstance(self.zone, str):
            self.zone = str(self.zone)

        if self._is_empty(self.start_time):
            self.MissingRequiredField("start_time")
        if not isinstance(self.start_time, str):
            self.start_time = str(self.start_time)

        if self._is_empty(self.cpus):
            self.MissingRequiredField("cpus")
        if not isinstance(self.cpus, int):
            self.cpus = int(self.cpus)

        if self._is_empty(self.stop_time):
            self.MissingRequiredField("stop_time")
        if not isinstance(self.stop_time, str):
            self.stop_time = str(self.stop_time)

        if self._is_empty(self.memory):
            self.MissingRequiredField("memory")
        if not isinstance(self.memory, str):
            self.memory = str(self.memory)

        if self._is_empty(self.docker_image):
            self.MissingRequiredField("docker_image")
        if not isinstance(self.docker_image, str):
            self.docker_image = str(self.docker_image)

        if self.log_err is not None and not isinstance(self.log_err, str):
            self.log_err = str(self.log_err)

        if self.log_out is not None and not isinstance(self.log_out, str):
            self.log_out = str(self.log_out)

        super().__post_init__(**kwargs)


@dataclass
class Parameter(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_PROCESS.Parameter
    class_class_curie: ClassVar[str] = "Analysis_process:Parameter"
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = HCA.Parameter

    parameter_name: str = None
    parameter_value: str = None
    checksum: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.parameter_name):
            self.MissingRequiredField("parameter_name")
        if not isinstance(self.parameter_name, str):
            self.parameter_name = str(self.parameter_name)

        if self._is_empty(self.parameter_value):
            self.MissingRequiredField("parameter_value")
        if not isinstance(self.parameter_value, str):
            self.parameter_value = str(self.parameter_value)

        if self.checksum is not None and not isinstance(self.checksum, str):
            self.checksum = str(self.checksum)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_PROCESS.AnalysisProcess
    class_class_curie: ClassVar[str] = "Analysis_process:AnalysisProcess"
    class_name: ClassVar[str] = "AnalysisProcess"
    class_model_uri: ClassVar[URIRef] = HCA.AnalysisProcess

    describedBy: str = None
    schema_type: Union[str, "AnalysisProcessSchemaTypeOptions"] = None
    process_core: Union[dict, ProcessCore] = None
    type: Union[dict, ProcessTypeOntology] = None
    inputs: Union[Union[dict, Parameter], List[Union[dict, Parameter]]] = None
    tasks: Union[Union[dict, Task], List[Union[dict, Task]]] = None
    timestamp_start_utc: str = None
    timestamp_stop_utc: str = None
    analysis_run_type: Union[str, "AnalysisProcessAnalysisRunTypeOptions"] = None
    reference_files: Union[str, List[str]] = None
    schema_version: Optional[str] = None
    provenance: Optional[Union[dict, Provenance]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.describedBy):
            self.MissingRequiredField("describedBy")
        if not isinstance(self.describedBy, str):
            self.describedBy = str(self.describedBy)

        if self._is_empty(self.schema_type):
            self.MissingRequiredField("schema_type")
        if not isinstance(self.schema_type, AnalysisProcessSchemaTypeOptions):
            self.schema_type = AnalysisProcessSchemaTypeOptions(self.schema_type)

        if self._is_empty(self.process_core):
            self.MissingRequiredField("process_core")
        if not isinstance(self.process_core, ProcessCore):
            self.process_core = ProcessCore(**as_dict(self.process_core))

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, ProcessTypeOntology):
            self.type = ProcessTypeOntology(**as_dict(self.type))

        if self._is_empty(self.inputs):
            self.MissingRequiredField("inputs")
        self._normalize_inlined_as_dict(slot_name="inputs", slot_type=Parameter, key_name="parameter_name", keyed=False)

        if self._is_empty(self.tasks):
            self.MissingRequiredField("tasks")
        self._normalize_inlined_as_dict(slot_name="tasks", slot_type=Task, key_name="disk_size", keyed=False)

        if self._is_empty(self.timestamp_start_utc):
            self.MissingRequiredField("timestamp_start_utc")
        if not isinstance(self.timestamp_start_utc, str):
            self.timestamp_start_utc = str(self.timestamp_start_utc)

        if self._is_empty(self.timestamp_stop_utc):
            self.MissingRequiredField("timestamp_stop_utc")
        if not isinstance(self.timestamp_stop_utc, str):
            self.timestamp_stop_utc = str(self.timestamp_stop_utc)

        if self._is_empty(self.analysis_run_type):
            self.MissingRequiredField("analysis_run_type")
        if not isinstance(self.analysis_run_type, AnalysisProcessAnalysisRunTypeOptions):
            self.analysis_run_type = AnalysisProcessAnalysisRunTypeOptions(self.analysis_run_type)

        if self._is_empty(self.reference_files):
            self.MissingRequiredField("reference_files")
        if not isinstance(self.reference_files, list):
            self.reference_files = [self.reference_files] if self.reference_files is not None else []
        self.reference_files = [v if isinstance(v, str) else str(v) for v in self.reference_files]

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        super().__post_init__(**kwargs)


# Enumerations
class FileCoreFileSourceOptions(EnumDefinitionImpl):

    Contributor = PermissibleValue(text="Contributor")
    ArrayExpress = PermissibleValue(text="ArrayExpress")
    GEO = PermissibleValue(text="GEO")
    SCEA = PermissibleValue(text="SCEA")
    SCP = PermissibleValue(text="SCP")
    LungMAP = PermissibleValue(text="LungMAP")
    Zenodo = PermissibleValue(text="Zenodo")
    Publication = PermissibleValue(text="Publication")

    _defn = EnumDefinition(
        name="FileCoreFileSourceOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DCP/2 Analysis",
                PermissibleValue(text="DCP/2 Analysis") )
        setattr(cls, "HCA Release",
                PermissibleValue(text="HCA Release") )
        setattr(cls, "DCP/1 Matrix Service",
                PermissibleValue(text="DCP/1 Matrix Service") )
        setattr(cls, "DCP/2 Ingest",
                PermissibleValue(text="DCP/2 Ingest") )

class ChannelMultiplexedOptions(EnumDefinitionImpl):

    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")

    _defn = EnumDefinition(
        name="ChannelMultiplexedOptions",
    )

class DataNormalizationMethodsOptions(EnumDefinitionImpl):

    Downsampling = PermissibleValue(text="Downsampling")
    other = PermissibleValue(text="other")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="DataNormalizationMethodsOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CPM (counts per million)",
                PermissibleValue(text="CPM (counts per million)") )
        setattr(cls, "TPM (transcripts per kilobase million)",
                PermissibleValue(text="TPM (transcripts per kilobase million)") )
        setattr(cls, "RPKM (reads per kilobase of exon per million reads mapped)",
                PermissibleValue(text="RPKM (reads per kilobase of exon per million reads mapped)") )
        setattr(cls, "FPKM (fragments per kilobase of exon per million fragments mapped)",
                PermissibleValue(text="FPKM (fragments per kilobase of exon per million fragments mapped)") )
        setattr(cls, "DESeq2's median of ratios",
                PermissibleValue(text="DESeq2's median of ratios") )
        setattr(cls, "TMM (EdgeR's trimmed mean of M values)",
                PermissibleValue(text="TMM (EdgeR's trimmed mean of M values)") )
        setattr(cls, "SF (size factor)",
                PermissibleValue(text="SF (size factor)") )
        setattr(cls, "UQ (Upper quartile)",
                PermissibleValue(text="UQ (Upper quartile)") )

class DerivationProcessOptions(EnumDefinitionImpl):

    alignment = PermissibleValue(text="alignment")
    quantification = PermissibleValue(text="quantification")
    merging = PermissibleValue(text="merging")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="DerivationProcessOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "peak calling",
                PermissibleValue(text="peak calling") )
        setattr(cls, "peak annotation",
                PermissibleValue(text="peak annotation") )
        setattr(cls, "gene filtering",
                PermissibleValue(text="gene filtering") )
        setattr(cls, "cell filtering",
                PermissibleValue(text="cell filtering") )
        setattr(cls, "cell calling",
                PermissibleValue(text="cell calling") )
        setattr(cls, "ambient RNA correction",
                PermissibleValue(text="ambient RNA correction") )
        setattr(cls, "doublet removal",
                PermissibleValue(text="doublet removal") )
        setattr(cls, "batch correction",
                PermissibleValue(text="batch correction") )
        setattr(cls, "depth normalization",
                PermissibleValue(text="depth normalization") )

class FileContentOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="FileContentOntologyOntologyOptions",
    )

class LengthUnitOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LengthUnitOntologyOntologyOptions",
    )

class CellCycleOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellCycleOntologyOntologyOptions",
    )

class LibraryAmplificationOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LibraryAmplificationOntologyOntologyOptions",
    )

class ContributorRoleOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ContributorRoleOntologyOntologyOptions",
    )

class EthnicityOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EthnicityOntologyOntologyOptions",
    )

class TargetPathwayOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TargetPathwayOntologyOntologyOptions",
    )

class TreatmentMethodOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TreatmentMethodOntologyOntologyOptions",
    )

class CellularComponentOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellularComponentOntologyOntologyOptions",
    )

class LibraryConstructionOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LibraryConstructionOntologyOntologyOptions",
    )

class ProcessTypeOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ProcessTypeOntologyOntologyOptions",
    )

class SequencingOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SequencingOntologyOntologyOptions",
    )

class SpeciesOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SpeciesOntologyOntologyOptions",
    )

class DiseaseOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DiseaseOntologyOntologyOptions",
    )

class StrainOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StrainOntologyOntologyOptions",
    )

class FileFormatOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="FileFormatOntologyOntologyOptions",
    )

class EnrichmentOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnrichmentOntologyOntologyOptions",
    )

class OrganPartOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="OrganPartOntologyOntologyOptions",
    )

class MicroscopyOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MicroscopyOntologyOntologyOptions",
    )

class TimeUnitOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TimeUnitOntologyOntologyOptions",
    )

class ProtocolTypeOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ProtocolTypeOntologyOntologyOptions",
    )

class DevelopmentStageOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DevelopmentStageOntologyOntologyOptions",
    )

class InstrumentOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InstrumentOntologyOntologyOptions",
    )

class MassUnitOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MassUnitOntologyOntologyOptions",
    )

class BiologicalMacromoleculeOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="BiologicalMacromoleculeOntologyOntologyOptions",
    )

class CellTypeOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellTypeOntologyOntologyOptions",
    )

class OrganOntologyOntologyOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="OrganOntologyOntologyOptions",
    )

class GrowthConditionsMycoplasmaTestingMethodOptions(EnumDefinitionImpl):

    PCR = PermissibleValue(text="PCR")
    ELISA = PermissibleValue(text="ELISA")
    Autoradiography = PermissibleValue(text="Autoradiography")
    Immunostaining = PermissibleValue(text="Immunostaining")

    _defn = EnumDefinition(
        name="GrowthConditionsMycoplasmaTestingMethodOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Direct DNA stain",
                PermissibleValue(text="Direct DNA stain") )
        setattr(cls, "Indirect DNA stain",
                PermissibleValue(text="Indirect DNA stain") )
        setattr(cls, "Broth and agar culture",
                PermissibleValue(text="Broth and agar culture") )
        setattr(cls, "Nested PCR",
                PermissibleValue(text="Nested PCR") )
        setattr(cls, "Cell-based assay",
                PermissibleValue(text="Cell-based assay") )
        setattr(cls, "Microbiological assay",
                PermissibleValue(text="Microbiological assay") )

class GrowthConditionsMycoplasmaTestingResultsOptions(EnumDefinitionImpl):

    fail = PermissibleValue(text="fail")

    _defn = EnumDefinition(
        name="GrowthConditionsMycoplasmaTestingResultsOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "pass",
                PermissibleValue(text="pass") )

class GrowthConditionsFeederLayerTypeOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GrowthConditionsFeederLayerTypeOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "feeder-free",
                PermissibleValue(text="feeder-free") )
        setattr(cls, "feeder-dependent, JK1 feeder cells",
                PermissibleValue(text="feeder-dependent, JK1 feeder cells") )
        setattr(cls, "feeder-dependent, SNL 76/7 feeder cells",
                PermissibleValue(text="feeder-dependent, SNL 76/7 feeder cells") )
        setattr(cls, "feeder-dependent, human marrow stromal cells",
                PermissibleValue(text="feeder-dependent, human marrow stromal cells") )
        setattr(cls, "feeder-dependent, bovine embryonic fibroblast cells",
                PermissibleValue(text="feeder-dependent, bovine embryonic fibroblast cells") )
        setattr(cls, "feeder-dependent, mouse embryonic fibroblast cells",
                PermissibleValue(text="feeder-dependent, mouse embryonic fibroblast cells") )
        setattr(cls, "feeder-dependent, mouse fibroblast STO cells",
                PermissibleValue(text="feeder-dependent, mouse fibroblast STO cells") )
        setattr(cls, "feeder-dependent, mouse bone marrow stromal cells",
                PermissibleValue(text="feeder-dependent, mouse bone marrow stromal cells") )
        setattr(cls, "feeder-dependent, mouse yolk sac-derived endothelial cells",
                PermissibleValue(text="feeder-dependent, mouse yolk sac-derived endothelial cells") )
        setattr(cls, "feeder-dependent, human foreskin fibroblast cells",
                PermissibleValue(text="feeder-dependent, human foreskin fibroblast cells") )
        setattr(cls, "feeder-dependent, human newborn fibroblast cells",
                PermissibleValue(text="feeder-dependent, human newborn fibroblast cells") )
        setattr(cls, "feeder-dependent, human fetal lung fibroblast cells",
                PermissibleValue(text="feeder-dependent, human fetal lung fibroblast cells") )
        setattr(cls, "feeder-dependent, human uterine endometrial cells",
                PermissibleValue(text="feeder-dependent, human uterine endometrial cells") )
        setattr(cls, "feeder-dependent, human breast parenchymal cells",
                PermissibleValue(text="feeder-dependent, human breast parenchymal cells") )
        setattr(cls, "feeder-dependent, human embryonic fibroblast cells",
                PermissibleValue(text="feeder-dependent, human embryonic fibroblast cells") )
        setattr(cls, "feeder-dependent, human adipose stromal cells",
                PermissibleValue(text="feeder-dependent, human adipose stromal cells") )
        setattr(cls, "feeder-dependent, human amniotic epithelial cells",
                PermissibleValue(text="feeder-dependent, human amniotic epithelial cells") )
        setattr(cls, "feeder-dependent, human placental fibroblast cells",
                PermissibleValue(text="feeder-dependent, human placental fibroblast cells") )
        setattr(cls, "feeder-dependent, human umbilical cord stromal cells",
                PermissibleValue(text="feeder-dependent, human umbilical cord stromal cells") )
        setattr(cls, "feeder-dependent, human fetal muscle cells",
                PermissibleValue(text="feeder-dependent, human fetal muscle cells") )
        setattr(cls, "feeder-dependent, human fetal skin cells",
                PermissibleValue(text="feeder-dependent, human fetal skin cells") )
        setattr(cls, "feeder-dependent, human fetal liver stromal cells",
                PermissibleValue(text="feeder-dependent, human fetal liver stromal cells") )
        setattr(cls, "feeder-dependent, human fallopian tubal epithelial cells",
                PermissibleValue(text="feeder-dependent, human fallopian tubal epithelial cells") )
        setattr(cls, "feeder-dependent, human amniotic mesenchymal cells",
                PermissibleValue(text="feeder-dependent, human amniotic mesenchymal cells") )

class PreservationStorageStorageMethodOptions(EnumDefinitionImpl):

    fresh = PermissibleValue(text="fresh")

    _defn = EnumDefinition(
        name="PreservationStorageStorageMethodOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ambient temperature",
                PermissibleValue(text="ambient temperature") )
        setattr(cls, "cut slide",
                PermissibleValue(text="cut slide") )
        setattr(cls, "frozen at -70C",
                PermissibleValue(text="frozen at -70C") )
        setattr(cls, "frozen at -80C",
                PermissibleValue(text="frozen at -80C") )
        setattr(cls, "frozen at -150C",
                PermissibleValue(text="frozen at -150C") )
        setattr(cls, "frozen in liquid nitrogen",
                PermissibleValue(text="frozen in liquid nitrogen") )
        setattr(cls, "frozen in vapor phase",
                PermissibleValue(text="frozen in vapor phase") )
        setattr(cls, "paraffin block",
                PermissibleValue(text="paraffin block") )
        setattr(cls, "RNAlater at 4C",
                PermissibleValue(text="RNAlater at 4C") )
        setattr(cls, "RNAlater at 25C",
                PermissibleValue(text="RNAlater at 25C") )
        setattr(cls, "RNAlater at -20C",
                PermissibleValue(text="RNAlater at -20C") )

class PreservationStoragePreservationMethodOptions(EnumDefinitionImpl):

    fresh = PermissibleValue(text="fresh")

    _defn = EnumDefinition(
        name="PreservationStoragePreservationMethodOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cryopreservation in liquid nitrogen (dead tissue)",
                PermissibleValue(text="cryopreservation in liquid nitrogen (dead tissue)") )
        setattr(cls, "cryopreservation in dry ice (dead tissue)",
                PermissibleValue(text="cryopreservation in dry ice (dead tissue)") )
        setattr(cls, "cryopreservation of live cells in liquid nitrogen",
                PermissibleValue(text="cryopreservation of live cells in liquid nitrogen") )
        setattr(cls, "cryopreservation, other",
                PermissibleValue(text="cryopreservation, other") )
        setattr(cls, "formalin fixed, unbuffered",
                PermissibleValue(text="formalin fixed, unbuffered") )
        setattr(cls, "formalin fixed, buffered",
                PermissibleValue(text="formalin fixed, buffered") )
        setattr(cls, "formalin fixed and paraffin embedded",
                PermissibleValue(text="formalin fixed and paraffin embedded") )
        setattr(cls, "hypothermic preservation media at 2-8C",
                PermissibleValue(text="hypothermic preservation media at 2-8C") )

class DeathOrganDonationDeathTypeOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DeathOrganDonationDeathTypeOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Donation after circulatory death (DCD)",
                PermissibleValue(text="Donation after circulatory death (DCD)") )
        setattr(cls, "Donation after brainstem death (DBD)",
                PermissibleValue(text="Donation after brainstem death (DBD)") )

class DeathNormothermicRegionalPerfusionOptions(EnumDefinitionImpl):

    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="DeathNormothermicRegionalPerfusionOptions",
    )

class MedicalHistoryNutritionalStateOptions(EnumDefinitionImpl):

    normal = PermissibleValue(text="normal")
    fasting = PermissibleValue(text="fasting")

    _defn = EnumDefinition(
        name="MedicalHistoryNutritionalStateOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "feeding tube removed",
                PermissibleValue(text="feeding tube removed") )

class CellMorphologyCellViabilityResultOptions(EnumDefinitionImpl):

    fail = PermissibleValue(text="fail")

    _defn = EnumDefinition(
        name="CellMorphologyCellViabilityResultOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "pass",
                PermissibleValue(text="pass") )

class StateOfSpecimenAutolysisScoreOptions(EnumDefinitionImpl):

    none = PermissibleValue(text="none")
    mild = PermissibleValue(text="mild")
    moderate = PermissibleValue(text="moderate")

    _defn = EnumDefinition(
        name="StateOfSpecimenAutolysisScoreOptions",
    )

class StateOfSpecimenIschemicTemperatureOptions(EnumDefinitionImpl):

    warm = PermissibleValue(text="warm")
    cold = PermissibleValue(text="cold")

    _defn = EnumDefinition(
        name="StateOfSpecimenIschemicTemperatureOptions",
    )

class BarcodeBarcodeReadOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="BarcodeBarcodeReadOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Read 1",
                PermissibleValue(text="Read 1") )
        setattr(cls, "Read 2",
                PermissibleValue(text="Read 2") )
        setattr(cls, "Read 3",
                PermissibleValue(text="Read 3") )
        setattr(cls, "Read 4",
                PermissibleValue(text="Read 4") )
        setattr(cls, "i7 Index",
                PermissibleValue(text="i7 Index") )
        setattr(cls, "i5 Index",
                PermissibleValue(text="i5 Index") )

class PlateBasedSequencingWellQualityOptions(EnumDefinitionImpl):

    OK = PermissibleValue(text="OK")

    _defn = EnumDefinition(
        name="PlateBasedSequencingWellQualityOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "control, 2-cell well",
                PermissibleValue(text="control, 2-cell well") )
        setattr(cls, "control, empty well",
                PermissibleValue(text="control, empty well") )
        setattr(cls, "low quality cell",
                PermissibleValue(text="low quality cell") )

class FileDescriptorSchemaTypeOptions(EnumDefinitionImpl):

    file_descriptor = PermissibleValue(text="file_descriptor")

    _defn = EnumDefinition(
        name="FileDescriptorSchemaTypeOptions",
    )

class ProtocolReferenceProtocolTypeOptions(EnumDefinitionImpl):

    analysis_protocol = PermissibleValue(text="analysis_protocol")
    aggregate_generation_protocol = PermissibleValue(text="aggregate_generation_protocol")
    collection_protocol = PermissibleValue(text="collection_protocol")
    differentiation_protocol = PermissibleValue(text="differentiation_protocol")
    dissociation_protocol = PermissibleValue(text="dissociation_protocol")
    enrichment_protocol = PermissibleValue(text="enrichment_protocol")
    ipsc_induction_protocol = PermissibleValue(text="ipsc_induction_protocol")
    imaging_preparation_protocol = PermissibleValue(text="imaging_preparation_protocol")
    imaging_protocol = PermissibleValue(text="imaging_protocol")
    library_preparation_protocol = PermissibleValue(text="library_preparation_protocol")
    sequencing_protocol = PermissibleValue(text="sequencing_protocol")
    treatment_protocol = PermissibleValue(text="treatment_protocol")

    _defn = EnumDefinition(
        name="ProtocolReferenceProtocolTypeOptions",
    )

class ProcessLinkLinkTypeOptions(EnumDefinitionImpl):

    process_link = PermissibleValue(text="process_link")

    _defn = EnumDefinition(
        name="ProcessLinkLinkTypeOptions",
    )

class SupplementaryFileEntityFileTypeOptions(EnumDefinitionImpl):

    supplementary_file = PermissibleValue(text="supplementary_file")

    _defn = EnumDefinition(
        name="SupplementaryFileEntityFileTypeOptions",
    )

class EntityEntityTypeOptions(EnumDefinitionImpl):

    project = PermissibleValue(text="project")

    _defn = EnumDefinition(
        name="EntityEntityTypeOptions",
    )

class SupplementaryFileLinkLinkTypeOptions(EnumDefinitionImpl):

    supplementary_file_link = PermissibleValue(text="supplementary_file_link")

    _defn = EnumDefinition(
        name="SupplementaryFileLinkLinkTypeOptions",
    )

class LinksSchemaTypeOptions(EnumDefinitionImpl):

    links = PermissibleValue(text="links")

    _defn = EnumDefinition(
        name="LinksSchemaTypeOptions",
    )

class SequenceFileSchemaTypeOptions(EnumDefinitionImpl):

    file = PermissibleValue(text="file")

    _defn = EnumDefinition(
        name="SequenceFileSchemaTypeOptions",
    )

class SequenceFileReadIndexOptions(EnumDefinitionImpl):

    read1 = PermissibleValue(text="read1")
    read2 = PermissibleValue(text="read2")
    read3 = PermissibleValue(text="read3")
    read4 = PermissibleValue(text="read4")
    index1 = PermissibleValue(text="index1")
    index2 = PermissibleValue(text="index2")

    _defn = EnumDefinition(
        name="SequenceFileReadIndexOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "single-end, non-indexed",
                PermissibleValue(text="single-end, non-indexed") )

class ImageFileSchemaTypeOptions(EnumDefinitionImpl):

    file = PermissibleValue(text="file")

    _defn = EnumDefinition(
        name="ImageFileSchemaTypeOptions",
    )

class SupplementaryFileSchemaTypeOptions(EnumDefinitionImpl):

    file = PermissibleValue(text="file")

    _defn = EnumDefinition(
        name="SupplementaryFileSchemaTypeOptions",
    )

class AnalysisFileSchemaTypeOptions(EnumDefinitionImpl):

    file = PermissibleValue(text="file")

    _defn = EnumDefinition(
        name="AnalysisFileSchemaTypeOptions",
    )

class ReferenceFileSchemaTypeOptions(EnumDefinitionImpl):

    file = PermissibleValue(text="file")

    _defn = EnumDefinition(
        name="ReferenceFileSchemaTypeOptions",
    )

class ReferenceFileReferenceTypeOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ReferenceFileReferenceTypeOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "genome sequence",
                PermissibleValue(text="genome sequence") )
        setattr(cls, "transcriptome sequence",
                PermissibleValue(text="transcriptome sequence") )
        setattr(cls, "annotation reference",
                PermissibleValue(text="annotation reference") )
        setattr(cls, "transcriptome index",
                PermissibleValue(text="transcriptome index") )
        setattr(cls, "genome sequence index",
                PermissibleValue(text="genome sequence index") )

class ReferenceFileAssemblyTypeOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ReferenceFileAssemblyTypeOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "primary assembly",
                PermissibleValue(text="primary assembly") )
        setattr(cls, "complete assembly",
                PermissibleValue(text="complete assembly") )
        setattr(cls, "patch assembly",
                PermissibleValue(text="patch assembly") )

class ProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="ProtocolSchemaTypeOptions",
    )

class SequencingProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="SequencingProtocolSchemaTypeOptions",
    )

class LibraryPreparationProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="LibraryPreparationProtocolSchemaTypeOptions",
    )

class LibraryPreparationProtocolNucleicAcidSourceOptions(EnumDefinitionImpl):

    mitochondria = PermissibleValue(text="mitochondria")

    _defn = EnumDefinition(
        name="LibraryPreparationProtocolNucleicAcidSourceOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "bulk cell",
                PermissibleValue(text="bulk cell") )
        setattr(cls, "single cell",
                PermissibleValue(text="single cell") )
        setattr(cls, "single nucleus",
                PermissibleValue(text="single nucleus") )
        setattr(cls, "bulk nuclei",
                PermissibleValue(text="bulk nuclei") )

class LibraryPreparationProtocolEndBiasOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LibraryPreparationProtocolEndBiasOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "3 prime tag",
                PermissibleValue(text="3 prime tag") )
        setattr(cls, "3 prime end bias",
                PermissibleValue(text="3 prime end bias") )
        setattr(cls, "5 prime tag",
                PermissibleValue(text="5 prime tag") )
        setattr(cls, "5 prime end bias",
                PermissibleValue(text="5 prime end bias") )
        setattr(cls, "full length",
                PermissibleValue(text="full length") )

class LibraryPreparationProtocolPrimerOptions(EnumDefinitionImpl):

    random = PermissibleValue(text="random")

    _defn = EnumDefinition(
        name="LibraryPreparationProtocolPrimerOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "poly-dT",
                PermissibleValue(text="poly-dT") )

class LibraryPreparationProtocolStrandOptions(EnumDefinitionImpl):

    first = PermissibleValue(text="first")
    second = PermissibleValue(text="second")
    unstranded = PermissibleValue(text="unstranded")

    _defn = EnumDefinition(
        name="LibraryPreparationProtocolStrandOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not provided",
                PermissibleValue(text="not provided") )

class AnalysisProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="AnalysisProtocolSchemaTypeOptions",
    )

class AggregateGenerationProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="AggregateGenerationProtocolSchemaTypeOptions",
    )

class EnrichmentProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="EnrichmentProtocolSchemaTypeOptions",
    )

class DissociationProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="DissociationProtocolSchemaTypeOptions",
    )

class IpscInductionProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="IpscInductionProtocolSchemaTypeOptions",
    )

class IpscInductionProtocolMethodOptions(EnumDefinitionImpl):

    lentivirus = PermissibleValue(text="lentivirus")
    adenovirus = PermissibleValue(text="adenovirus")
    plasmid = PermissibleValue(text="plasmid")
    retroviral = PermissibleValue(text="retroviral")

    _defn = EnumDefinition(
        name="IpscInductionProtocolMethodOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "sendai virus",
                PermissibleValue(text="sendai virus") )
        setattr(cls, "Gun particle",
                PermissibleValue(text="Gun particle") )
        setattr(cls, "piggyBac transposon",
                PermissibleValue(text="piggyBac transposon") )
        setattr(cls, "miRNA viral",
                PermissibleValue(text="miRNA viral") )
        setattr(cls, "cre-loxP",
                PermissibleValue(text="cre-loxP") )

class IpscInductionProtocolPluripotencyVectorRemovedOptions(EnumDefinitionImpl):

    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="IpscInductionProtocolPluripotencyVectorRemovedOptions",
    )

class CollectionProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="CollectionProtocolSchemaTypeOptions",
    )

class DifferentiationProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="DifferentiationProtocolSchemaTypeOptions",
    )

class TreatmentProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="TreatmentProtocolSchemaTypeOptions",
    )

class ImagingPreparationProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="ImagingPreparationProtocolSchemaTypeOptions",
    )

class ImagingProtocolSchemaTypeOptions(EnumDefinitionImpl):

    protocol = PermissibleValue(text="protocol")

    _defn = EnumDefinition(
        name="ImagingProtocolSchemaTypeOptions",
    )

class ImagingProtocolOverlappingTilesOptions(EnumDefinitionImpl):

    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")

    _defn = EnumDefinition(
        name="ImagingProtocolOverlappingTilesOptions",
    )

class ProjectSchemaTypeOptions(EnumDefinitionImpl):

    project = PermissibleValue(text="project")

    _defn = EnumDefinition(
        name="ProjectSchemaTypeOptions",
    )

class SpecimenFromOrganismSchemaTypeOptions(EnumDefinitionImpl):

    biomaterial = PermissibleValue(text="biomaterial")

    _defn = EnumDefinition(
        name="SpecimenFromOrganismSchemaTypeOptions",
    )

class CellSuspensionSchemaTypeOptions(EnumDefinitionImpl):

    biomaterial = PermissibleValue(text="biomaterial")

    _defn = EnumDefinition(
        name="CellSuspensionSchemaTypeOptions",
    )

class CellLineSchemaTypeOptions(EnumDefinitionImpl):

    biomaterial = PermissibleValue(text="biomaterial")

    _defn = EnumDefinition(
        name="CellLineSchemaTypeOptions",
    )

class CellLineTypeOptions(EnumDefinitionImpl):

    primary = PermissibleValue(text="primary")
    immortalized = PermissibleValue(text="immortalized")
    synthetic = PermissibleValue(text="synthetic")

    _defn = EnumDefinition(
        name="CellLineTypeOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "stem cell",
                PermissibleValue(text="stem cell") )
        setattr(cls, "stem cell-derived",
                PermissibleValue(text="stem cell-derived") )
        setattr(cls, "induced pluripotent",
                PermissibleValue(text="induced pluripotent") )

class ImagedSpecimenSchemaTypeOptions(EnumDefinitionImpl):

    biomaterial = PermissibleValue(text="biomaterial")

    _defn = EnumDefinition(
        name="ImagedSpecimenSchemaTypeOptions",
    )

class DonorOrganismSchemaTypeOptions(EnumDefinitionImpl):

    biomaterial = PermissibleValue(text="biomaterial")

    _defn = EnumDefinition(
        name="DonorOrganismSchemaTypeOptions",
    )

class DonorOrganismSexOptions(EnumDefinitionImpl):

    female = PermissibleValue(text="female")
    male = PermissibleValue(text="male")
    mixed = PermissibleValue(text="mixed")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="DonorOrganismSexOptions",
    )

class DonorOrganismIsLivingOptions(EnumDefinitionImpl):

    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="DonorOrganismIsLivingOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not applicable",
                PermissibleValue(text="not applicable") )

class OrganoidSchemaTypeOptions(EnumDefinitionImpl):

    biomaterial = PermissibleValue(text="biomaterial")

    _defn = EnumDefinition(
        name="OrganoidSchemaTypeOptions",
    )

class ProcessSchemaTypeOptions(EnumDefinitionImpl):

    process = PermissibleValue(text="process")

    _defn = EnumDefinition(
        name="ProcessSchemaTypeOptions",
    )

class AnalysisProcessSchemaTypeOptions(EnumDefinitionImpl):

    process = PermissibleValue(text="process")

    _defn = EnumDefinition(
        name="AnalysisProcessSchemaTypeOptions",
    )

class AnalysisProcessAnalysisRunTypeOptions(EnumDefinitionImpl):

    run = PermissibleValue(text="run")

    _defn = EnumDefinition(
        name="AnalysisProcessAnalysisRunTypeOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "copy-forward",
                PermissibleValue(text="copy-forward") )

# Slots
class slots:
    pass

slots.fileCore__describedBy = Slot(uri=HCA.describedBy, name="fileCore__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.fileCore__describedBy, domain=None, range=Optional[str])

slots.fileCore__schema_version = Slot(uri=HCA.schema_version, name="fileCore__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.fileCore__schema_version, domain=None, range=Optional[str])

slots.fileCore__file_name = Slot(uri=HCA.file_name, name="fileCore__file_name", curie=HCA.curie('file_name'),
                   model_uri=HCA.fileCore__file_name, domain=None, range=str)

slots.fileCore__format = Slot(uri=HCA.format, name="fileCore__format", curie=HCA.curie('format'),
                   model_uri=HCA.fileCore__format, domain=None, range=str)

slots.fileCore__content_description = Slot(uri=HCA.content_description, name="fileCore__content_description", curie=HCA.curie('content_description'),
                   model_uri=HCA.fileCore__content_description, domain=None, range=Optional[Union[Union[dict, FileContentOntology], List[Union[dict, FileContentOntology]]]])

slots.fileCore__checksum = Slot(uri=HCA.checksum, name="fileCore__checksum", curie=HCA.curie('checksum'),
                   model_uri=HCA.fileCore__checksum, domain=None, range=Optional[str])

slots.fileCore__file_source = Slot(uri=HCA.file_source, name="fileCore__file_source", curie=HCA.curie('file_source'),
                   model_uri=HCA.fileCore__file_source, domain=None, range=Optional[Union[str, "FileCoreFileSourceOptions"]])

slots.protocolCore__describedBy = Slot(uri=HCA.describedBy, name="protocolCore__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.protocolCore__describedBy, domain=None, range=Optional[str])

slots.protocolCore__schema_version = Slot(uri=HCA.schema_version, name="protocolCore__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.protocolCore__schema_version, domain=None, range=Optional[str])

slots.protocolCore__protocol_id = Slot(uri=HCA.protocol_id, name="protocolCore__protocol_id", curie=HCA.curie('protocol_id'),
                   model_uri=HCA.protocolCore__protocol_id, domain=None, range=str)

slots.protocolCore__protocol_name = Slot(uri=HCA.protocol_name, name="protocolCore__protocol_name", curie=HCA.curie('protocol_name'),
                   model_uri=HCA.protocolCore__protocol_name, domain=None, range=Optional[str])

slots.protocolCore__protocol_description = Slot(uri=HCA.protocol_description, name="protocolCore__protocol_description", curie=HCA.curie('protocol_description'),
                   model_uri=HCA.protocolCore__protocol_description, domain=None, range=Optional[str])

slots.protocolCore__publication_doi = Slot(uri=HCA.publication_doi, name="protocolCore__publication_doi", curie=HCA.curie('publication_doi'),
                   model_uri=HCA.protocolCore__publication_doi, domain=None, range=Optional[str])

slots.protocolCore__protocols_io_doi = Slot(uri=HCA.protocols_io_doi, name="protocolCore__protocols_io_doi", curie=HCA.curie('protocols_io_doi'),
                   model_uri=HCA.protocolCore__protocols_io_doi, domain=None, range=Optional[str])

slots.protocolCore__document = Slot(uri=HCA.document, name="protocolCore__document", curie=HCA.curie('document'),
                   model_uri=HCA.protocolCore__document, domain=None, range=Optional[str])

slots.projectCore__describedBy = Slot(uri=HCA.describedBy, name="projectCore__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.projectCore__describedBy, domain=None, range=Optional[str])

slots.projectCore__schema_version = Slot(uri=HCA.schema_version, name="projectCore__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.projectCore__schema_version, domain=None, range=Optional[str])

slots.projectCore__project_short_name = Slot(uri=HCA.project_short_name, name="projectCore__project_short_name", curie=HCA.curie('project_short_name'),
                   model_uri=HCA.projectCore__project_short_name, domain=None, range=str)

slots.projectCore__project_title = Slot(uri=HCA.project_title, name="projectCore__project_title", curie=HCA.curie('project_title'),
                   model_uri=HCA.projectCore__project_title, domain=None, range=str)

slots.projectCore__project_description = Slot(uri=HCA.project_description, name="projectCore__project_description", curie=HCA.curie('project_description'),
                   model_uri=HCA.projectCore__project_description, domain=None, range=str)

slots.biomaterialCore__describedBy = Slot(uri=HCA.describedBy, name="biomaterialCore__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.biomaterialCore__describedBy, domain=None, range=Optional[str])

slots.biomaterialCore__schema_version = Slot(uri=HCA.schema_version, name="biomaterialCore__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.biomaterialCore__schema_version, domain=None, range=Optional[str])

slots.biomaterialCore__biomaterial_id = Slot(uri=HCA.biomaterial_id, name="biomaterialCore__biomaterial_id", curie=HCA.curie('biomaterial_id'),
                   model_uri=HCA.biomaterialCore__biomaterial_id, domain=None, range=str)

slots.biomaterialCore__biomaterial_name = Slot(uri=HCA.biomaterial_name, name="biomaterialCore__biomaterial_name", curie=HCA.curie('biomaterial_name'),
                   model_uri=HCA.biomaterialCore__biomaterial_name, domain=None, range=Optional[str])

slots.biomaterialCore__biomaterial_description = Slot(uri=HCA.biomaterial_description, name="biomaterialCore__biomaterial_description", curie=HCA.curie('biomaterial_description'),
                   model_uri=HCA.biomaterialCore__biomaterial_description, domain=None, range=Optional[str])

slots.biomaterialCore__ncbi_taxon_id = Slot(uri=HCA.ncbi_taxon_id, name="biomaterialCore__ncbi_taxon_id", curie=HCA.curie('ncbi_taxon_id'),
                   model_uri=HCA.biomaterialCore__ncbi_taxon_id, domain=None, range=Union[int, List[int]])

slots.biomaterialCore__genotype = Slot(uri=HCA.genotype, name="biomaterialCore__genotype", curie=HCA.curie('genotype'),
                   model_uri=HCA.biomaterialCore__genotype, domain=None, range=Optional[str])

slots.biomaterialCore__supplementary_files = Slot(uri=HCA.supplementary_files, name="biomaterialCore__supplementary_files", curie=HCA.curie('supplementary_files'),
                   model_uri=HCA.biomaterialCore__supplementary_files, domain=None, range=Optional[Union[str, List[str]]])

slots.biomaterialCore__biosamples_accession = Slot(uri=HCA.biosamples_accession, name="biomaterialCore__biosamples_accession", curie=HCA.curie('biosamples_accession'),
                   model_uri=HCA.biomaterialCore__biosamples_accession, domain=None, range=Optional[str])

slots.biomaterialCore__insdc_sample_accession = Slot(uri=HCA.insdc_sample_accession, name="biomaterialCore__insdc_sample_accession", curie=HCA.curie('insdc_sample_accession'),
                   model_uri=HCA.biomaterialCore__insdc_sample_accession, domain=None, range=Optional[str])

slots.biomaterialCore__HDBR_accession = Slot(uri=HCA.HDBR_accession, name="biomaterialCore__HDBR_accession", curie=HCA.curie('HDBR_accession'),
                   model_uri=HCA.biomaterialCore__HDBR_accession, domain=None, range=Optional[str])

slots.processCore__describedBy = Slot(uri=HCA.describedBy, name="processCore__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.processCore__describedBy, domain=None, range=Optional[str])

slots.processCore__schema_version = Slot(uri=HCA.schema_version, name="processCore__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.processCore__schema_version, domain=None, range=Optional[str])

slots.processCore__process_id = Slot(uri=HCA.process_id, name="processCore__process_id", curie=HCA.curie('process_id'),
                   model_uri=HCA.processCore__process_id, domain=None, range=str)

slots.processCore__process_name = Slot(uri=HCA.process_name, name="processCore__process_name", curie=HCA.curie('process_name'),
                   model_uri=HCA.processCore__process_name, domain=None, range=Optional[str])

slots.processCore__process_description = Slot(uri=HCA.process_description, name="processCore__process_description", curie=HCA.curie('process_description'),
                   model_uri=HCA.processCore__process_description, domain=None, range=Optional[str])

slots.processCore__location = Slot(uri=HCA.location, name="processCore__location", curie=HCA.curie('location'),
                   model_uri=HCA.processCore__location, domain=None, range=Optional[str])

slots.processCore__operators = Slot(uri=HCA.operators, name="processCore__operators", curie=HCA.curie('operators'),
                   model_uri=HCA.processCore__operators, domain=None, range=Optional[Union[str, List[str]]])

slots.channel__describedBy = Slot(uri=HCA.describedBy, name="channel__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.channel__describedBy, domain=None, range=Optional[str])

slots.channel__schema_version = Slot(uri=HCA.schema_version, name="channel__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.channel__schema_version, domain=None, range=Optional[str])

slots.channel__channel_id = Slot(uri=HCA.channel_id, name="channel__channel_id", curie=HCA.curie('channel_id'),
                   model_uri=HCA.channel__channel_id, domain=None, range=str)

slots.channel__excitation_wavelength = Slot(uri=HCA.excitation_wavelength, name="channel__excitation_wavelength", curie=HCA.curie('excitation_wavelength'),
                   model_uri=HCA.channel__excitation_wavelength, domain=None, range=float)

slots.channel__filter_range = Slot(uri=HCA.filter_range, name="channel__filter_range", curie=HCA.curie('filter_range'),
                   model_uri=HCA.channel__filter_range, domain=None, range=str)

slots.channel__multiplexed = Slot(uri=HCA.multiplexed, name="channel__multiplexed", curie=HCA.curie('multiplexed'),
                   model_uri=HCA.channel__multiplexed, domain=None, range=Union[str, "ChannelMultiplexedOptions"])

slots.channel__target_fluorophore = Slot(uri=HCA.target_fluorophore, name="channel__target_fluorophore", curie=HCA.curie('target_fluorophore'),
                   model_uri=HCA.channel__target_fluorophore, domain=None, range=Optional[str])

slots.channel__exposure_time = Slot(uri=HCA.exposure_time, name="channel__exposure_time", curie=HCA.curie('exposure_time'),
                   model_uri=HCA.channel__exposure_time, domain=None, range=float)

slots.probe__describedBy = Slot(uri=HCA.describedBy, name="probe__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.probe__describedBy, domain=None, range=Optional[str])

slots.probe__schema_version = Slot(uri=HCA.schema_version, name="probe__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.probe__schema_version, domain=None, range=Optional[str])

slots.probe__probe_label = Slot(uri=HCA.probe_label, name="probe__probe_label", curie=HCA.curie('probe_label'),
                   model_uri=HCA.probe__probe_label, domain=None, range=str)

slots.probe__probe_sequence = Slot(uri=HCA.probe_sequence, name="probe__probe_sequence", curie=HCA.curie('probe_sequence'),
                   model_uri=HCA.probe__probe_sequence, domain=None, range=Optional[str])

slots.probe__target_name = Slot(uri=HCA.target_name, name="probe__target_name", curie=HCA.curie('target_name'),
                   model_uri=HCA.probe__target_name, domain=None, range=Optional[str])

slots.probe__target_codebook_label = Slot(uri=HCA.target_codebook_label, name="probe__target_codebook_label", curie=HCA.curie('target_codebook_label'),
                   model_uri=HCA.probe__target_codebook_label, domain=None, range=Optional[str])

slots.probe__target_label = Slot(uri=HCA.target_label, name="probe__target_label", curie=HCA.curie('target_label'),
                   model_uri=HCA.probe__target_label, domain=None, range=str)

slots.probe__subcellular_structure = Slot(uri=HCA.subcellular_structure, name="probe__subcellular_structure", curie=HCA.curie('subcellular_structure'),
                   model_uri=HCA.probe__subcellular_structure, domain=None, range=Optional[Union[dict, CellularComponentOntology]])

slots.probe__probe_reagents = Slot(uri=HCA.probe_reagents, name="probe__probe_reagents", curie=HCA.curie('probe_reagents'),
                   model_uri=HCA.probe__probe_reagents, domain=None, range=Optional[Union[dict, PurchasedReagents]])

slots.probe__assay_type = Slot(uri=HCA.assay_type, name="probe__assay_type", curie=HCA.curie('assay_type'),
                   model_uri=HCA.probe__assay_type, domain=None, range=Union[dict, ProcessTypeOntology])

slots.probe__fluorophore = Slot(uri=HCA.fluorophore, name="probe__fluorophore", curie=HCA.curie('fluorophore'),
                   model_uri=HCA.probe__fluorophore, domain=None, range=Optional[Union[str, List[str]]])

slots.probe__channel_label = Slot(uri=HCA.channel_label, name="probe__channel_label", curie=HCA.curie('channel_label'),
                   model_uri=HCA.probe__channel_label, domain=None, range=Optional[Union[str, List[str]]])

slots.matrix__describedBy = Slot(uri=HCA.describedBy, name="matrix__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.matrix__describedBy, domain=None, range=Optional[str])

slots.matrix__schema_version = Slot(uri=HCA.schema_version, name="matrix__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.matrix__schema_version, domain=None, range=Optional[str])

slots.matrix__data_normalization_methods = Slot(uri=HCA.data_normalization_methods, name="matrix__data_normalization_methods", curie=HCA.curie('data_normalization_methods'),
                   model_uri=HCA.matrix__data_normalization_methods, domain=None, range=Optional[Union[Union[str, "DataNormalizationMethodsOptions"], List[Union[str, "DataNormalizationMethodsOptions"]]]])

slots.matrix__derivation_process = Slot(uri=HCA.derivation_process, name="matrix__derivation_process", curie=HCA.curie('derivation_process'),
                   model_uri=HCA.matrix__derivation_process, domain=None, range=Optional[Union[Union[str, "DerivationProcessOptions"], List[Union[str, "DerivationProcessOptions"]]]])

slots.fileContentOntology__describedBy = Slot(uri=HCA.describedBy, name="fileContentOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.fileContentOntology__describedBy, domain=None, range=Optional[str])

slots.fileContentOntology__schema_version = Slot(uri=HCA.schema_version, name="fileContentOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.fileContentOntology__schema_version, domain=None, range=Optional[str])

slots.fileContentOntology__text = Slot(uri=HCA.text, name="fileContentOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.fileContentOntology__text, domain=None, range=str)

slots.fileContentOntology__ontology = Slot(uri=HCA.ontology, name="fileContentOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.fileContentOntology__ontology, domain=None, range=Optional[Union[str, "FileContentOntologyOntologyOptions"]])

slots.fileContentOntology__ontology_label = Slot(uri=HCA.ontology_label, name="fileContentOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.fileContentOntology__ontology_label, domain=None, range=Optional[str])

slots.lengthUnitOntology__describedBy = Slot(uri=HCA.describedBy, name="lengthUnitOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.lengthUnitOntology__describedBy, domain=None, range=Optional[str])

slots.lengthUnitOntology__schema_version = Slot(uri=HCA.schema_version, name="lengthUnitOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.lengthUnitOntology__schema_version, domain=None, range=Optional[str])

slots.lengthUnitOntology__text = Slot(uri=HCA.text, name="lengthUnitOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.lengthUnitOntology__text, domain=None, range=str)

slots.lengthUnitOntology__ontology = Slot(uri=HCA.ontology, name="lengthUnitOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.lengthUnitOntology__ontology, domain=None, range=Optional[Union[str, "LengthUnitOntologyOntologyOptions"]])

slots.lengthUnitOntology__ontology_label = Slot(uri=HCA.ontology_label, name="lengthUnitOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.lengthUnitOntology__ontology_label, domain=None, range=Optional[str])

slots.cellCycleOntology__describedBy = Slot(uri=HCA.describedBy, name="cellCycleOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.cellCycleOntology__describedBy, domain=None, range=Optional[str])

slots.cellCycleOntology__schema_version = Slot(uri=HCA.schema_version, name="cellCycleOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.cellCycleOntology__schema_version, domain=None, range=Optional[str])

slots.cellCycleOntology__text = Slot(uri=HCA.text, name="cellCycleOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.cellCycleOntology__text, domain=None, range=str)

slots.cellCycleOntology__ontology = Slot(uri=HCA.ontology, name="cellCycleOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.cellCycleOntology__ontology, domain=None, range=Optional[Union[str, "CellCycleOntologyOntologyOptions"]])

slots.cellCycleOntology__ontology_label = Slot(uri=HCA.ontology_label, name="cellCycleOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.cellCycleOntology__ontology_label, domain=None, range=Optional[str])

slots.libraryAmplificationOntology__describedBy = Slot(uri=HCA.describedBy, name="libraryAmplificationOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.libraryAmplificationOntology__describedBy, domain=None, range=Optional[str])

slots.libraryAmplificationOntology__schema_version = Slot(uri=HCA.schema_version, name="libraryAmplificationOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.libraryAmplificationOntology__schema_version, domain=None, range=Optional[str])

slots.libraryAmplificationOntology__text = Slot(uri=HCA.text, name="libraryAmplificationOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.libraryAmplificationOntology__text, domain=None, range=str)

slots.libraryAmplificationOntology__ontology = Slot(uri=HCA.ontology, name="libraryAmplificationOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.libraryAmplificationOntology__ontology, domain=None, range=Optional[Union[str, "LibraryAmplificationOntologyOntologyOptions"]])

slots.libraryAmplificationOntology__ontology_label = Slot(uri=HCA.ontology_label, name="libraryAmplificationOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.libraryAmplificationOntology__ontology_label, domain=None, range=Optional[str])

slots.contributorRoleOntology__describedBy = Slot(uri=HCA.describedBy, name="contributorRoleOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.contributorRoleOntology__describedBy, domain=None, range=Optional[str])

slots.contributorRoleOntology__schema_version = Slot(uri=HCA.schema_version, name="contributorRoleOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.contributorRoleOntology__schema_version, domain=None, range=Optional[str])

slots.contributorRoleOntology__text = Slot(uri=HCA.text, name="contributorRoleOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.contributorRoleOntology__text, domain=None, range=str)

slots.contributorRoleOntology__ontology = Slot(uri=HCA.ontology, name="contributorRoleOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.contributorRoleOntology__ontology, domain=None, range=Optional[Union[str, "ContributorRoleOntologyOntologyOptions"]])

slots.contributorRoleOntology__ontology_label = Slot(uri=HCA.ontology_label, name="contributorRoleOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.contributorRoleOntology__ontology_label, domain=None, range=Optional[str])

slots.ethnicityOntology__describedBy = Slot(uri=HCA.describedBy, name="ethnicityOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.ethnicityOntology__describedBy, domain=None, range=Optional[str])

slots.ethnicityOntology__schema_version = Slot(uri=HCA.schema_version, name="ethnicityOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.ethnicityOntology__schema_version, domain=None, range=Optional[str])

slots.ethnicityOntology__text = Slot(uri=HCA.text, name="ethnicityOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.ethnicityOntology__text, domain=None, range=str)

slots.ethnicityOntology__ontology = Slot(uri=HCA.ontology, name="ethnicityOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.ethnicityOntology__ontology, domain=None, range=Optional[Union[str, "EthnicityOntologyOntologyOptions"]])

slots.ethnicityOntology__ontology_label = Slot(uri=HCA.ontology_label, name="ethnicityOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.ethnicityOntology__ontology_label, domain=None, range=Optional[str])

slots.targetPathwayOntology__describedBy = Slot(uri=HCA.describedBy, name="targetPathwayOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.targetPathwayOntology__describedBy, domain=None, range=Optional[str])

slots.targetPathwayOntology__schema_version = Slot(uri=HCA.schema_version, name="targetPathwayOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.targetPathwayOntology__schema_version, domain=None, range=Optional[str])

slots.targetPathwayOntology__text = Slot(uri=HCA.text, name="targetPathwayOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.targetPathwayOntology__text, domain=None, range=str)

slots.targetPathwayOntology__ontology = Slot(uri=HCA.ontology, name="targetPathwayOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.targetPathwayOntology__ontology, domain=None, range=Optional[Union[str, "TargetPathwayOntologyOntologyOptions"]])

slots.targetPathwayOntology__ontology_label = Slot(uri=HCA.ontology_label, name="targetPathwayOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.targetPathwayOntology__ontology_label, domain=None, range=Optional[str])

slots.treatmentMethodOntology__describedBy = Slot(uri=HCA.describedBy, name="treatmentMethodOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.treatmentMethodOntology__describedBy, domain=None, range=Optional[str])

slots.treatmentMethodOntology__schema_version = Slot(uri=HCA.schema_version, name="treatmentMethodOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.treatmentMethodOntology__schema_version, domain=None, range=Optional[str])

slots.treatmentMethodOntology__text = Slot(uri=HCA.text, name="treatmentMethodOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.treatmentMethodOntology__text, domain=None, range=str)

slots.treatmentMethodOntology__ontology = Slot(uri=HCA.ontology, name="treatmentMethodOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.treatmentMethodOntology__ontology, domain=None, range=Optional[Union[str, "TreatmentMethodOntologyOntologyOptions"]])

slots.treatmentMethodOntology__ontology_label = Slot(uri=HCA.ontology_label, name="treatmentMethodOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.treatmentMethodOntology__ontology_label, domain=None, range=Optional[str])

slots.cellularComponentOntology__describedBy = Slot(uri=HCA.describedBy, name="cellularComponentOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.cellularComponentOntology__describedBy, domain=None, range=Optional[str])

slots.cellularComponentOntology__schema_version = Slot(uri=HCA.schema_version, name="cellularComponentOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.cellularComponentOntology__schema_version, domain=None, range=Optional[str])

slots.cellularComponentOntology__text = Slot(uri=HCA.text, name="cellularComponentOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.cellularComponentOntology__text, domain=None, range=str)

slots.cellularComponentOntology__ontology = Slot(uri=HCA.ontology, name="cellularComponentOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.cellularComponentOntology__ontology, domain=None, range=Optional[Union[str, "CellularComponentOntologyOntologyOptions"]])

slots.cellularComponentOntology__ontology_label = Slot(uri=HCA.ontology_label, name="cellularComponentOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.cellularComponentOntology__ontology_label, domain=None, range=Optional[str])

slots.libraryConstructionOntology__describedBy = Slot(uri=HCA.describedBy, name="libraryConstructionOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.libraryConstructionOntology__describedBy, domain=None, range=Optional[str])

slots.libraryConstructionOntology__schema_version = Slot(uri=HCA.schema_version, name="libraryConstructionOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.libraryConstructionOntology__schema_version, domain=None, range=Optional[str])

slots.libraryConstructionOntology__text = Slot(uri=HCA.text, name="libraryConstructionOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.libraryConstructionOntology__text, domain=None, range=str)

slots.libraryConstructionOntology__ontology = Slot(uri=HCA.ontology, name="libraryConstructionOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.libraryConstructionOntology__ontology, domain=None, range=Optional[Union[str, "LibraryConstructionOntologyOntologyOptions"]])

slots.libraryConstructionOntology__ontology_label = Slot(uri=HCA.ontology_label, name="libraryConstructionOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.libraryConstructionOntology__ontology_label, domain=None, range=Optional[str])

slots.processTypeOntology__describedBy = Slot(uri=HCA.describedBy, name="processTypeOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.processTypeOntology__describedBy, domain=None, range=Optional[str])

slots.processTypeOntology__schema_version = Slot(uri=HCA.schema_version, name="processTypeOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.processTypeOntology__schema_version, domain=None, range=Optional[str])

slots.processTypeOntology__text = Slot(uri=HCA.text, name="processTypeOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.processTypeOntology__text, domain=None, range=str)

slots.processTypeOntology__ontology = Slot(uri=HCA.ontology, name="processTypeOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.processTypeOntology__ontology, domain=None, range=Optional[Union[str, "ProcessTypeOntologyOntologyOptions"]])

slots.processTypeOntology__ontology_label = Slot(uri=HCA.ontology_label, name="processTypeOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.processTypeOntology__ontology_label, domain=None, range=Optional[str])

slots.sequencingOntology__describedBy = Slot(uri=HCA.describedBy, name="sequencingOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.sequencingOntology__describedBy, domain=None, range=Optional[str])

slots.sequencingOntology__schema_version = Slot(uri=HCA.schema_version, name="sequencingOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.sequencingOntology__schema_version, domain=None, range=Optional[str])

slots.sequencingOntology__text = Slot(uri=HCA.text, name="sequencingOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.sequencingOntology__text, domain=None, range=str)

slots.sequencingOntology__ontology = Slot(uri=HCA.ontology, name="sequencingOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.sequencingOntology__ontology, domain=None, range=Optional[Union[str, "SequencingOntologyOntologyOptions"]])

slots.sequencingOntology__ontology_label = Slot(uri=HCA.ontology_label, name="sequencingOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.sequencingOntology__ontology_label, domain=None, range=Optional[str])

slots.speciesOntology__describedBy = Slot(uri=HCA.describedBy, name="speciesOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.speciesOntology__describedBy, domain=None, range=Optional[str])

slots.speciesOntology__schema_version = Slot(uri=HCA.schema_version, name="speciesOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.speciesOntology__schema_version, domain=None, range=Optional[str])

slots.speciesOntology__text = Slot(uri=HCA.text, name="speciesOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.speciesOntology__text, domain=None, range=str)

slots.speciesOntology__ontology = Slot(uri=HCA.ontology, name="speciesOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.speciesOntology__ontology, domain=None, range=Optional[Union[str, "SpeciesOntologyOntologyOptions"]])

slots.speciesOntology__ontology_label = Slot(uri=HCA.ontology_label, name="speciesOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.speciesOntology__ontology_label, domain=None, range=Optional[str])

slots.diseaseOntology__describedBy = Slot(uri=HCA.describedBy, name="diseaseOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.diseaseOntology__describedBy, domain=None, range=Optional[str])

slots.diseaseOntology__schema_version = Slot(uri=HCA.schema_version, name="diseaseOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.diseaseOntology__schema_version, domain=None, range=Optional[str])

slots.diseaseOntology__text = Slot(uri=HCA.text, name="diseaseOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.diseaseOntology__text, domain=None, range=str)

slots.diseaseOntology__ontology = Slot(uri=HCA.ontology, name="diseaseOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.diseaseOntology__ontology, domain=None, range=Optional[Union[str, "DiseaseOntologyOntologyOptions"]])

slots.diseaseOntology__ontology_label = Slot(uri=HCA.ontology_label, name="diseaseOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.diseaseOntology__ontology_label, domain=None, range=Optional[str])

slots.strainOntology__describedBy = Slot(uri=HCA.describedBy, name="strainOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.strainOntology__describedBy, domain=None, range=Optional[str])

slots.strainOntology__schema_version = Slot(uri=HCA.schema_version, name="strainOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.strainOntology__schema_version, domain=None, range=Optional[str])

slots.strainOntology__text = Slot(uri=HCA.text, name="strainOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.strainOntology__text, domain=None, range=str)

slots.strainOntology__ontology = Slot(uri=HCA.ontology, name="strainOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.strainOntology__ontology, domain=None, range=Optional[Union[str, "StrainOntologyOntologyOptions"]])

slots.strainOntology__ontology_label = Slot(uri=HCA.ontology_label, name="strainOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.strainOntology__ontology_label, domain=None, range=Optional[str])

slots.fileFormatOntology__describedBy = Slot(uri=HCA.describedBy, name="fileFormatOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.fileFormatOntology__describedBy, domain=None, range=Optional[str])

slots.fileFormatOntology__schema_version = Slot(uri=HCA.schema_version, name="fileFormatOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.fileFormatOntology__schema_version, domain=None, range=Optional[str])

slots.fileFormatOntology__text = Slot(uri=HCA.text, name="fileFormatOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.fileFormatOntology__text, domain=None, range=str)

slots.fileFormatOntology__ontology = Slot(uri=HCA.ontology, name="fileFormatOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.fileFormatOntology__ontology, domain=None, range=Optional[Union[str, "FileFormatOntologyOntologyOptions"]])

slots.fileFormatOntology__ontology_label = Slot(uri=HCA.ontology_label, name="fileFormatOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.fileFormatOntology__ontology_label, domain=None, range=Optional[str])

slots.enrichmentOntology__describedBy = Slot(uri=HCA.describedBy, name="enrichmentOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.enrichmentOntology__describedBy, domain=None, range=Optional[str])

slots.enrichmentOntology__schema_version = Slot(uri=HCA.schema_version, name="enrichmentOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.enrichmentOntology__schema_version, domain=None, range=Optional[str])

slots.enrichmentOntology__text = Slot(uri=HCA.text, name="enrichmentOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.enrichmentOntology__text, domain=None, range=str)

slots.enrichmentOntology__ontology = Slot(uri=HCA.ontology, name="enrichmentOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.enrichmentOntology__ontology, domain=None, range=Optional[Union[str, "EnrichmentOntologyOntologyOptions"]])

slots.enrichmentOntology__ontology_label = Slot(uri=HCA.ontology_label, name="enrichmentOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.enrichmentOntology__ontology_label, domain=None, range=Optional[str])

slots.organPartOntology__describedBy = Slot(uri=HCA.describedBy, name="organPartOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.organPartOntology__describedBy, domain=None, range=Optional[str])

slots.organPartOntology__schema_version = Slot(uri=HCA.schema_version, name="organPartOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.organPartOntology__schema_version, domain=None, range=Optional[str])

slots.organPartOntology__text = Slot(uri=HCA.text, name="organPartOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.organPartOntology__text, domain=None, range=str)

slots.organPartOntology__ontology = Slot(uri=HCA.ontology, name="organPartOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.organPartOntology__ontology, domain=None, range=Optional[Union[str, "OrganPartOntologyOntologyOptions"]])

slots.organPartOntology__ontology_label = Slot(uri=HCA.ontology_label, name="organPartOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.organPartOntology__ontology_label, domain=None, range=Optional[str])

slots.microscopyOntology__describedBy = Slot(uri=HCA.describedBy, name="microscopyOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.microscopyOntology__describedBy, domain=None, range=Optional[str])

slots.microscopyOntology__schema_version = Slot(uri=HCA.schema_version, name="microscopyOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.microscopyOntology__schema_version, domain=None, range=Optional[str])

slots.microscopyOntology__text = Slot(uri=HCA.text, name="microscopyOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.microscopyOntology__text, domain=None, range=str)

slots.microscopyOntology__ontology = Slot(uri=HCA.ontology, name="microscopyOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.microscopyOntology__ontology, domain=None, range=Optional[Union[str, "MicroscopyOntologyOntologyOptions"]])

slots.microscopyOntology__ontology_label = Slot(uri=HCA.ontology_label, name="microscopyOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.microscopyOntology__ontology_label, domain=None, range=Optional[str])

slots.timeUnitOntology__describedBy = Slot(uri=HCA.describedBy, name="timeUnitOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.timeUnitOntology__describedBy, domain=None, range=Optional[str])

slots.timeUnitOntology__schema_version = Slot(uri=HCA.schema_version, name="timeUnitOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.timeUnitOntology__schema_version, domain=None, range=Optional[str])

slots.timeUnitOntology__text = Slot(uri=HCA.text, name="timeUnitOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.timeUnitOntology__text, domain=None, range=str)

slots.timeUnitOntology__ontology = Slot(uri=HCA.ontology, name="timeUnitOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.timeUnitOntology__ontology, domain=None, range=Optional[Union[str, "TimeUnitOntologyOntologyOptions"]])

slots.timeUnitOntology__ontology_label = Slot(uri=HCA.ontology_label, name="timeUnitOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.timeUnitOntology__ontology_label, domain=None, range=Optional[str])

slots.protocolTypeOntology__describedBy = Slot(uri=HCA.describedBy, name="protocolTypeOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.protocolTypeOntology__describedBy, domain=None, range=Optional[str])

slots.protocolTypeOntology__schema_version = Slot(uri=HCA.schema_version, name="protocolTypeOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.protocolTypeOntology__schema_version, domain=None, range=Optional[str])

slots.protocolTypeOntology__text = Slot(uri=HCA.text, name="protocolTypeOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.protocolTypeOntology__text, domain=None, range=str)

slots.protocolTypeOntology__ontology = Slot(uri=HCA.ontology, name="protocolTypeOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.protocolTypeOntology__ontology, domain=None, range=Optional[Union[str, "ProtocolTypeOntologyOntologyOptions"]])

slots.protocolTypeOntology__ontology_label = Slot(uri=HCA.ontology_label, name="protocolTypeOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.protocolTypeOntology__ontology_label, domain=None, range=Optional[str])

slots.developmentStageOntology__describedBy = Slot(uri=HCA.describedBy, name="developmentStageOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.developmentStageOntology__describedBy, domain=None, range=Optional[str])

slots.developmentStageOntology__schema_version = Slot(uri=HCA.schema_version, name="developmentStageOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.developmentStageOntology__schema_version, domain=None, range=Optional[str])

slots.developmentStageOntology__text = Slot(uri=HCA.text, name="developmentStageOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.developmentStageOntology__text, domain=None, range=str)

slots.developmentStageOntology__ontology = Slot(uri=HCA.ontology, name="developmentStageOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.developmentStageOntology__ontology, domain=None, range=Optional[Union[str, "DevelopmentStageOntologyOntologyOptions"]])

slots.developmentStageOntology__ontology_label = Slot(uri=HCA.ontology_label, name="developmentStageOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.developmentStageOntology__ontology_label, domain=None, range=Optional[str])

slots.instrumentOntology__describedBy = Slot(uri=HCA.describedBy, name="instrumentOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.instrumentOntology__describedBy, domain=None, range=Optional[str])

slots.instrumentOntology__schema_version = Slot(uri=HCA.schema_version, name="instrumentOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.instrumentOntology__schema_version, domain=None, range=Optional[str])

slots.instrumentOntology__text = Slot(uri=HCA.text, name="instrumentOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.instrumentOntology__text, domain=None, range=str)

slots.instrumentOntology__ontology = Slot(uri=HCA.ontology, name="instrumentOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.instrumentOntology__ontology, domain=None, range=Optional[Union[str, "InstrumentOntologyOntologyOptions"]])

slots.instrumentOntology__ontology_label = Slot(uri=HCA.ontology_label, name="instrumentOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.instrumentOntology__ontology_label, domain=None, range=Optional[str])

slots.massUnitOntology__describedBy = Slot(uri=HCA.describedBy, name="massUnitOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.massUnitOntology__describedBy, domain=None, range=Optional[str])

slots.massUnitOntology__schema_version = Slot(uri=HCA.schema_version, name="massUnitOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.massUnitOntology__schema_version, domain=None, range=Optional[str])

slots.massUnitOntology__text = Slot(uri=HCA.text, name="massUnitOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.massUnitOntology__text, domain=None, range=str)

slots.massUnitOntology__ontology = Slot(uri=HCA.ontology, name="massUnitOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.massUnitOntology__ontology, domain=None, range=Optional[Union[str, "MassUnitOntologyOntologyOptions"]])

slots.massUnitOntology__ontology_label = Slot(uri=HCA.ontology_label, name="massUnitOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.massUnitOntology__ontology_label, domain=None, range=Optional[str])

slots.biologicalMacromoleculeOntology__describedBy = Slot(uri=HCA.describedBy, name="biologicalMacromoleculeOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.biologicalMacromoleculeOntology__describedBy, domain=None, range=Optional[str])

slots.biologicalMacromoleculeOntology__schema_version = Slot(uri=HCA.schema_version, name="biologicalMacromoleculeOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.biologicalMacromoleculeOntology__schema_version, domain=None, range=Optional[str])

slots.biologicalMacromoleculeOntology__text = Slot(uri=HCA.text, name="biologicalMacromoleculeOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.biologicalMacromoleculeOntology__text, domain=None, range=str)

slots.biologicalMacromoleculeOntology__ontology = Slot(uri=HCA.ontology, name="biologicalMacromoleculeOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.biologicalMacromoleculeOntology__ontology, domain=None, range=Optional[Union[str, "BiologicalMacromoleculeOntologyOntologyOptions"]])

slots.biologicalMacromoleculeOntology__ontology_label = Slot(uri=HCA.ontology_label, name="biologicalMacromoleculeOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.biologicalMacromoleculeOntology__ontology_label, domain=None, range=Optional[str])

slots.cellTypeOntology__describedBy = Slot(uri=HCA.describedBy, name="cellTypeOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.cellTypeOntology__describedBy, domain=None, range=Optional[str])

slots.cellTypeOntology__schema_version = Slot(uri=HCA.schema_version, name="cellTypeOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.cellTypeOntology__schema_version, domain=None, range=Optional[str])

slots.cellTypeOntology__text = Slot(uri=HCA.text, name="cellTypeOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.cellTypeOntology__text, domain=None, range=str)

slots.cellTypeOntology__ontology = Slot(uri=HCA.ontology, name="cellTypeOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.cellTypeOntology__ontology, domain=None, range=Optional[Union[str, "CellTypeOntologyOntologyOptions"]])

slots.cellTypeOntology__ontology_label = Slot(uri=HCA.ontology_label, name="cellTypeOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.cellTypeOntology__ontology_label, domain=None, range=Optional[str])

slots.organOntology__describedBy = Slot(uri=HCA.describedBy, name="organOntology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.organOntology__describedBy, domain=None, range=Optional[str])

slots.organOntology__schema_version = Slot(uri=HCA.schema_version, name="organOntology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.organOntology__schema_version, domain=None, range=Optional[str])

slots.organOntology__text = Slot(uri=HCA.text, name="organOntology__text", curie=HCA.curie('text'),
                   model_uri=HCA.organOntology__text, domain=None, range=str)

slots.organOntology__ontology = Slot(uri=HCA.ontology, name="organOntology__ontology", curie=HCA.curie('ontology'),
                   model_uri=HCA.organOntology__ontology, domain=None, range=Optional[Union[str, "OrganOntologyOntologyOptions"]])

slots.organOntology__ontology_label = Slot(uri=HCA.ontology_label, name="organOntology__ontology_label", curie=HCA.curie('ontology_label'),
                   model_uri=HCA.organOntology__ontology_label, domain=None, range=Optional[str])

slots.funder__describedBy = Slot(uri=HCA.describedBy, name="funder__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.funder__describedBy, domain=None, range=Optional[str])

slots.funder__schema_version = Slot(uri=HCA.schema_version, name="funder__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.funder__schema_version, domain=None, range=Optional[str])

slots.funder__grant_title = Slot(uri=HCA.grant_title, name="funder__grant_title", curie=HCA.curie('grant_title'),
                   model_uri=HCA.funder__grant_title, domain=None, range=Optional[str])

slots.funder__grant_id = Slot(uri=HCA.grant_id, name="funder__grant_id", curie=HCA.curie('grant_id'),
                   model_uri=HCA.funder__grant_id, domain=None, range=str)

slots.funder__organization = Slot(uri=HCA.organization, name="funder__organization", curie=HCA.curie('organization'),
                   model_uri=HCA.funder__organization, domain=None, range=str)

slots.contact__describedBy = Slot(uri=HCA.describedBy, name="contact__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.contact__describedBy, domain=None, range=Optional[str])

slots.contact__schema_version = Slot(uri=HCA.schema_version, name="contact__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.contact__schema_version, domain=None, range=Optional[str])

slots.contact__email = Slot(uri=HCA.email, name="contact__email", curie=HCA.curie('email'),
                   model_uri=HCA.contact__email, domain=None, range=Optional[str])

slots.contact__phone = Slot(uri=HCA.phone, name="contact__phone", curie=HCA.curie('phone'),
                   model_uri=HCA.contact__phone, domain=None, range=Optional[str])

slots.contact__institution = Slot(uri=HCA.institution, name="contact__institution", curie=HCA.curie('institution'),
                   model_uri=HCA.contact__institution, domain=None, range=str)

slots.contact__laboratory = Slot(uri=HCA.laboratory, name="contact__laboratory", curie=HCA.curie('laboratory'),
                   model_uri=HCA.contact__laboratory, domain=None, range=Optional[str])

slots.contact__address = Slot(uri=HCA.address, name="contact__address", curie=HCA.curie('address'),
                   model_uri=HCA.contact__address, domain=None, range=Optional[str])

slots.contact__country = Slot(uri=HCA.country, name="contact__country", curie=HCA.curie('country'),
                   model_uri=HCA.contact__country, domain=None, range=Optional[str])

slots.contact__corresponding_contributor = Slot(uri=HCA.corresponding_contributor, name="contact__corresponding_contributor", curie=HCA.curie('corresponding_contributor'),
                   model_uri=HCA.contact__corresponding_contributor, domain=None, range=Optional[Union[bool, Bool]])

slots.contact__project_role = Slot(uri=HCA.project_role, name="contact__project_role", curie=HCA.curie('project_role'),
                   model_uri=HCA.contact__project_role, domain=None, range=Optional[Union[dict, ContributorRoleOntology]])

slots.contact__orcid_id = Slot(uri=HCA.orcid_id, name="contact__orcid_id", curie=HCA.curie('orcid_id'),
                   model_uri=HCA.contact__orcid_id, domain=None, range=Optional[str])

slots.publication__describedBy = Slot(uri=HCA.describedBy, name="publication__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.publication__describedBy, domain=None, range=Optional[str])

slots.publication__schema_version = Slot(uri=HCA.schema_version, name="publication__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.publication__schema_version, domain=None, range=Optional[str])

slots.publication__authors = Slot(uri=HCA.authors, name="publication__authors", curie=HCA.curie('authors'),
                   model_uri=HCA.publication__authors, domain=None, range=Union[str, List[str]])

slots.publication__title = Slot(uri=HCA.title, name="publication__title", curie=HCA.curie('title'),
                   model_uri=HCA.publication__title, domain=None, range=str)

slots.publication__doi = Slot(uri=HCA.doi, name="publication__doi", curie=HCA.curie('doi'),
                   model_uri=HCA.publication__doi, domain=None, range=Optional[str])

slots.publication__pmid = Slot(uri=HCA.pmid, name="publication__pmid", curie=HCA.curie('pmid'),
                   model_uri=HCA.publication__pmid, domain=None, range=Optional[int])

slots.publication__url = Slot(uri=HCA.url, name="publication__url", curie=HCA.curie('url'),
                   model_uri=HCA.publication__url, domain=None, range=Optional[str])

slots.publication__official_hca_publication = Slot(uri=HCA.official_hca_publication, name="publication__official_hca_publication", curie=HCA.curie('official_hca_publication'),
                   model_uri=HCA.publication__official_hca_publication, domain=None, range=Union[bool, Bool])

slots.humanSpecific__describedBy = Slot(uri=HCA.describedBy, name="humanSpecific__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.humanSpecific__describedBy, domain=None, range=Optional[str])

slots.humanSpecific__schema_version = Slot(uri=HCA.schema_version, name="humanSpecific__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.humanSpecific__schema_version, domain=None, range=Optional[str])

slots.humanSpecific__body_mass_index = Slot(uri=HCA.body_mass_index, name="humanSpecific__body_mass_index", curie=HCA.curie('body_mass_index'),
                   model_uri=HCA.humanSpecific__body_mass_index, domain=None, range=Optional[float])

slots.humanSpecific__ethnicity = Slot(uri=HCA.ethnicity, name="humanSpecific__ethnicity", curie=HCA.curie('ethnicity'),
                   model_uri=HCA.humanSpecific__ethnicity, domain=None, range=Optional[Union[Union[dict, EthnicityOntology], List[Union[dict, EthnicityOntology]]]])

slots.growthConditions__describedBy = Slot(uri=HCA.describedBy, name="growthConditions__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.growthConditions__describedBy, domain=None, range=Optional[str])

slots.growthConditions__schema_version = Slot(uri=HCA.schema_version, name="growthConditions__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.growthConditions__schema_version, domain=None, range=Optional[str])

slots.growthConditions__passage_number = Slot(uri=HCA.passage_number, name="growthConditions__passage_number", curie=HCA.curie('passage_number'),
                   model_uri=HCA.growthConditions__passage_number, domain=None, range=Optional[int])

slots.growthConditions__growth_medium = Slot(uri=HCA.growth_medium, name="growthConditions__growth_medium", curie=HCA.curie('growth_medium'),
                   model_uri=HCA.growthConditions__growth_medium, domain=None, range=Optional[str])

slots.growthConditions__culture_environment = Slot(uri=HCA.culture_environment, name="growthConditions__culture_environment", curie=HCA.curie('culture_environment'),
                   model_uri=HCA.growthConditions__culture_environment, domain=None, range=Optional[str])

slots.growthConditions__mycoplasma_testing_method = Slot(uri=HCA.mycoplasma_testing_method, name="growthConditions__mycoplasma_testing_method", curie=HCA.curie('mycoplasma_testing_method'),
                   model_uri=HCA.growthConditions__mycoplasma_testing_method, domain=None, range=Optional[Union[str, "GrowthConditionsMycoplasmaTestingMethodOptions"]])

slots.growthConditions__mycoplasma_testing_results = Slot(uri=HCA.mycoplasma_testing_results, name="growthConditions__mycoplasma_testing_results", curie=HCA.curie('mycoplasma_testing_results'),
                   model_uri=HCA.growthConditions__mycoplasma_testing_results, domain=None, range=Optional[Union[str, "GrowthConditionsMycoplasmaTestingResultsOptions"]])

slots.growthConditions__drug_treatment = Slot(uri=HCA.drug_treatment, name="growthConditions__drug_treatment", curie=HCA.curie('drug_treatment'),
                   model_uri=HCA.growthConditions__drug_treatment, domain=None, range=Optional[str])

slots.growthConditions__feeder_layer_type = Slot(uri=HCA.feeder_layer_type, name="growthConditions__feeder_layer_type", curie=HCA.curie('feeder_layer_type'),
                   model_uri=HCA.growthConditions__feeder_layer_type, domain=None, range=Optional[Union[str, "GrowthConditionsFeederLayerTypeOptions"]])

slots.preservationStorage__describedBy = Slot(uri=HCA.describedBy, name="preservationStorage__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.preservationStorage__describedBy, domain=None, range=Optional[str])

slots.preservationStorage__schema_version = Slot(uri=HCA.schema_version, name="preservationStorage__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.preservationStorage__schema_version, domain=None, range=Optional[str])

slots.preservationStorage__storage_method = Slot(uri=HCA.storage_method, name="preservationStorage__storage_method", curie=HCA.curie('storage_method'),
                   model_uri=HCA.preservationStorage__storage_method, domain=None, range=Optional[Union[str, "PreservationStorageStorageMethodOptions"]])

slots.preservationStorage__storage_time = Slot(uri=HCA.storage_time, name="preservationStorage__storage_time", curie=HCA.curie('storage_time'),
                   model_uri=HCA.preservationStorage__storage_time, domain=None, range=Optional[float])

slots.preservationStorage__storage_time_unit = Slot(uri=HCA.storage_time_unit, name="preservationStorage__storage_time_unit", curie=HCA.curie('storage_time_unit'),
                   model_uri=HCA.preservationStorage__storage_time_unit, domain=None, range=Optional[Union[dict, TimeUnitOntology]])

slots.preservationStorage__preservation_method = Slot(uri=HCA.preservation_method, name="preservationStorage__preservation_method", curie=HCA.curie('preservation_method'),
                   model_uri=HCA.preservationStorage__preservation_method, domain=None, range=Optional[Union[str, "PreservationStoragePreservationMethodOptions"]])

slots.death__describedBy = Slot(uri=HCA.describedBy, name="death__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.death__describedBy, domain=None, range=Optional[str])

slots.death__schema_version = Slot(uri=HCA.schema_version, name="death__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.death__schema_version, domain=None, range=Optional[str])

slots.death__cause_of_death = Slot(uri=HCA.cause_of_death, name="death__cause_of_death", curie=HCA.curie('cause_of_death'),
                   model_uri=HCA.death__cause_of_death, domain=None, range=str)

slots.death__cold_perfused = Slot(uri=HCA.cold_perfused, name="death__cold_perfused", curie=HCA.curie('cold_perfused'),
                   model_uri=HCA.death__cold_perfused, domain=None, range=Optional[Union[bool, Bool]])

slots.death__days_on_ventilator = Slot(uri=HCA.days_on_ventilator, name="death__days_on_ventilator", curie=HCA.curie('days_on_ventilator'),
                   model_uri=HCA.death__days_on_ventilator, domain=None, range=Optional[float])

slots.death__hardy_scale = Slot(uri=HCA.hardy_scale, name="death__hardy_scale", curie=HCA.curie('hardy_scale'),
                   model_uri=HCA.death__hardy_scale, domain=None, range=Optional[int])

slots.death__time_of_death = Slot(uri=HCA.time_of_death, name="death__time_of_death", curie=HCA.curie('time_of_death'),
                   model_uri=HCA.death__time_of_death, domain=None, range=Optional[str])

slots.death__organ_donation_death_type = Slot(uri=HCA.organ_donation_death_type, name="death__organ_donation_death_type", curie=HCA.curie('organ_donation_death_type'),
                   model_uri=HCA.death__organ_donation_death_type, domain=None, range=Optional[Union[str, "DeathOrganDonationDeathTypeOptions"]])

slots.death__normothermic_regional_perfusion = Slot(uri=HCA.normothermic_regional_perfusion, name="death__normothermic_regional_perfusion", curie=HCA.curie('normothermic_regional_perfusion'),
                   model_uri=HCA.death__normothermic_regional_perfusion, domain=None, range=Optional[Union[str, "DeathNormothermicRegionalPerfusionOptions"]])

slots.familialRelationship__describedBy = Slot(uri=HCA.describedBy, name="familialRelationship__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.familialRelationship__describedBy, domain=None, range=Optional[str])

slots.familialRelationship__schema_version = Slot(uri=HCA.schema_version, name="familialRelationship__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.familialRelationship__schema_version, domain=None, range=Optional[str])

slots.familialRelationship__parent = Slot(uri=HCA.parent, name="familialRelationship__parent", curie=HCA.curie('parent'),
                   model_uri=HCA.familialRelationship__parent, domain=None, range=Optional[str])

slots.familialRelationship__child = Slot(uri=HCA.child, name="familialRelationship__child", curie=HCA.curie('child'),
                   model_uri=HCA.familialRelationship__child, domain=None, range=Optional[str])

slots.familialRelationship__sibling = Slot(uri=HCA.sibling, name="familialRelationship__sibling", curie=HCA.curie('sibling'),
                   model_uri=HCA.familialRelationship__sibling, domain=None, range=Optional[str])

slots.medicalHistory__describedBy = Slot(uri=HCA.describedBy, name="medicalHistory__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.medicalHistory__describedBy, domain=None, range=Optional[str])

slots.medicalHistory__schema_version = Slot(uri=HCA.schema_version, name="medicalHistory__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.medicalHistory__schema_version, domain=None, range=Optional[str])

slots.medicalHistory__alcohol_history = Slot(uri=HCA.alcohol_history, name="medicalHistory__alcohol_history", curie=HCA.curie('alcohol_history'),
                   model_uri=HCA.medicalHistory__alcohol_history, domain=None, range=Optional[str])

slots.medicalHistory__medication = Slot(uri=HCA.medication, name="medicalHistory__medication", curie=HCA.curie('medication'),
                   model_uri=HCA.medicalHistory__medication, domain=None, range=Optional[str])

slots.medicalHistory__smoking_history = Slot(uri=HCA.smoking_history, name="medicalHistory__smoking_history", curie=HCA.curie('smoking_history'),
                   model_uri=HCA.medicalHistory__smoking_history, domain=None, range=Optional[str])

slots.medicalHistory__nutritional_state = Slot(uri=HCA.nutritional_state, name="medicalHistory__nutritional_state", curie=HCA.curie('nutritional_state'),
                   model_uri=HCA.medicalHistory__nutritional_state, domain=None, range=Optional[Union[str, "MedicalHistoryNutritionalStateOptions"]])

slots.medicalHistory__test_results = Slot(uri=HCA.test_results, name="medicalHistory__test_results", curie=HCA.curie('test_results'),
                   model_uri=HCA.medicalHistory__test_results, domain=None, range=Optional[str])

slots.medicalHistory__treatment = Slot(uri=HCA.treatment, name="medicalHistory__treatment", curie=HCA.curie('treatment'),
                   model_uri=HCA.medicalHistory__treatment, domain=None, range=Optional[str])

slots.cellMorphology__describedBy = Slot(uri=HCA.describedBy, name="cellMorphology__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.cellMorphology__describedBy, domain=None, range=Optional[str])

slots.cellMorphology__schema_version = Slot(uri=HCA.schema_version, name="cellMorphology__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.cellMorphology__schema_version, domain=None, range=Optional[str])

slots.cellMorphology__cell_morphology = Slot(uri=HCA.cell_morphology, name="cellMorphology__cell_morphology", curie=HCA.curie('cell_morphology'),
                   model_uri=HCA.cellMorphology__cell_morphology, domain=None, range=Optional[str])

slots.cellMorphology__cell_size = Slot(uri=HCA.cell_size, name="cellMorphology__cell_size", curie=HCA.curie('cell_size'),
                   model_uri=HCA.cellMorphology__cell_size, domain=None, range=Optional[str])

slots.cellMorphology__cell_size_unit = Slot(uri=HCA.cell_size_unit, name="cellMorphology__cell_size_unit", curie=HCA.curie('cell_size_unit'),
                   model_uri=HCA.cellMorphology__cell_size_unit, domain=None, range=Optional[Union[dict, LengthUnitOntology]])

slots.cellMorphology__percent_cell_viability = Slot(uri=HCA.percent_cell_viability, name="cellMorphology__percent_cell_viability", curie=HCA.curie('percent_cell_viability'),
                   model_uri=HCA.cellMorphology__percent_cell_viability, domain=None, range=Optional[float])

slots.cellMorphology__cell_viability_method = Slot(uri=HCA.cell_viability_method, name="cellMorphology__cell_viability_method", curie=HCA.curie('cell_viability_method'),
                   model_uri=HCA.cellMorphology__cell_viability_method, domain=None, range=Optional[str])

slots.cellMorphology__cell_viability_result = Slot(uri=HCA.cell_viability_result, name="cellMorphology__cell_viability_result", curie=HCA.curie('cell_viability_result'),
                   model_uri=HCA.cellMorphology__cell_viability_result, domain=None, range=Optional[Union[str, "CellMorphologyCellViabilityResultOptions"]])

slots.cellMorphology__percent_necrosis = Slot(uri=HCA.percent_necrosis, name="cellMorphology__percent_necrosis", curie=HCA.curie('percent_necrosis'),
                   model_uri=HCA.cellMorphology__percent_necrosis, domain=None, range=Optional[float])

slots.stateOfSpecimen__describedBy = Slot(uri=HCA.describedBy, name="stateOfSpecimen__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.stateOfSpecimen__describedBy, domain=None, range=Optional[str])

slots.stateOfSpecimen__schema_version = Slot(uri=HCA.schema_version, name="stateOfSpecimen__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.stateOfSpecimen__schema_version, domain=None, range=Optional[str])

slots.stateOfSpecimen__autolysis_score = Slot(uri=HCA.autolysis_score, name="stateOfSpecimen__autolysis_score", curie=HCA.curie('autolysis_score'),
                   model_uri=HCA.stateOfSpecimen__autolysis_score, domain=None, range=Optional[Union[str, "StateOfSpecimenAutolysisScoreOptions"]])

slots.stateOfSpecimen__gross_description = Slot(uri=HCA.gross_description, name="stateOfSpecimen__gross_description", curie=HCA.curie('gross_description'),
                   model_uri=HCA.stateOfSpecimen__gross_description, domain=None, range=Optional[str])

slots.stateOfSpecimen__gross_images = Slot(uri=HCA.gross_images, name="stateOfSpecimen__gross_images", curie=HCA.curie('gross_images'),
                   model_uri=HCA.stateOfSpecimen__gross_images, domain=None, range=Optional[Union[str, List[str]]])

slots.stateOfSpecimen__ischemic_temperature = Slot(uri=HCA.ischemic_temperature, name="stateOfSpecimen__ischemic_temperature", curie=HCA.curie('ischemic_temperature'),
                   model_uri=HCA.stateOfSpecimen__ischemic_temperature, domain=None, range=Optional[Union[str, "StateOfSpecimenIschemicTemperatureOptions"]])

slots.stateOfSpecimen__ischemic_time = Slot(uri=HCA.ischemic_time, name="stateOfSpecimen__ischemic_time", curie=HCA.curie('ischemic_time'),
                   model_uri=HCA.stateOfSpecimen__ischemic_time, domain=None, range=Optional[int])

slots.stateOfSpecimen__microscopic_description = Slot(uri=HCA.microscopic_description, name="stateOfSpecimen__microscopic_description", curie=HCA.curie('microscopic_description'),
                   model_uri=HCA.stateOfSpecimen__microscopic_description, domain=None, range=Optional[str])

slots.stateOfSpecimen__microscopic_images = Slot(uri=HCA.microscopic_images, name="stateOfSpecimen__microscopic_images", curie=HCA.curie('microscopic_images'),
                   model_uri=HCA.stateOfSpecimen__microscopic_images, domain=None, range=Optional[Union[str, List[str]]])

slots.stateOfSpecimen__postmortem_interval = Slot(uri=HCA.postmortem_interval, name="stateOfSpecimen__postmortem_interval", curie=HCA.curie('postmortem_interval'),
                   model_uri=HCA.stateOfSpecimen__postmortem_interval, domain=None, range=Optional[int])

slots.timecourse__describedBy = Slot(uri=HCA.describedBy, name="timecourse__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.timecourse__describedBy, domain=None, range=Optional[str])

slots.timecourse__schema_version = Slot(uri=HCA.schema_version, name="timecourse__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.timecourse__schema_version, domain=None, range=Optional[str])

slots.timecourse__value = Slot(uri=HCA.value, name="timecourse__value", curie=HCA.curie('value'),
                   model_uri=HCA.timecourse__value, domain=None, range=str)

slots.timecourse__unit = Slot(uri=HCA.unit, name="timecourse__unit", curie=HCA.curie('unit'),
                   model_uri=HCA.timecourse__unit, domain=None, range=Union[dict, TimeUnitOntology])

slots.timecourse__relevance = Slot(uri=HCA.relevance, name="timecourse__relevance", curie=HCA.curie('relevance'),
                   model_uri=HCA.timecourse__relevance, domain=None, range=Optional[str])

slots.mouseSpecific__describedBy = Slot(uri=HCA.describedBy, name="mouseSpecific__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.mouseSpecific__describedBy, domain=None, range=Optional[str])

slots.mouseSpecific__schema_version = Slot(uri=HCA.schema_version, name="mouseSpecific__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.mouseSpecific__schema_version, domain=None, range=Optional[str])

slots.mouseSpecific__strain = Slot(uri=HCA.strain, name="mouseSpecific__strain", curie=HCA.curie('strain'),
                   model_uri=HCA.mouseSpecific__strain, domain=None, range=Optional[Union[Union[dict, StrainOntology], List[Union[dict, StrainOntology]]]])

slots.purchasedReagents__describedBy = Slot(uri=HCA.describedBy, name="purchasedReagents__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.purchasedReagents__describedBy, domain=None, range=Optional[str])

slots.purchasedReagents__schema_version = Slot(uri=HCA.schema_version, name="purchasedReagents__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.purchasedReagents__schema_version, domain=None, range=Optional[str])

slots.purchasedReagents__retail_name = Slot(uri=HCA.retail_name, name="purchasedReagents__retail_name", curie=HCA.curie('retail_name'),
                   model_uri=HCA.purchasedReagents__retail_name, domain=None, range=Optional[str])

slots.purchasedReagents__catalog_number = Slot(uri=HCA.catalog_number, name="purchasedReagents__catalog_number", curie=HCA.curie('catalog_number'),
                   model_uri=HCA.purchasedReagents__catalog_number, domain=None, range=Optional[str])

slots.purchasedReagents__manufacturer = Slot(uri=HCA.manufacturer, name="purchasedReagents__manufacturer", curie=HCA.curie('manufacturer'),
                   model_uri=HCA.purchasedReagents__manufacturer, domain=None, range=Optional[str])

slots.purchasedReagents__lot_number = Slot(uri=HCA.lot_number, name="purchasedReagents__lot_number", curie=HCA.curie('lot_number'),
                   model_uri=HCA.purchasedReagents__lot_number, domain=None, range=Optional[str])

slots.purchasedReagents__expiry_date = Slot(uri=HCA.expiry_date, name="purchasedReagents__expiry_date", curie=HCA.curie('expiry_date'),
                   model_uri=HCA.purchasedReagents__expiry_date, domain=None, range=Optional[str])

slots.purchasedReagents__kit_titer = Slot(uri=HCA.kit_titer, name="purchasedReagents__kit_titer", curie=HCA.curie('kit_titer'),
                   model_uri=HCA.purchasedReagents__kit_titer, domain=None, range=Optional[str])

slots.insdcExperiment__describedBy = Slot(uri=HCA.describedBy, name="insdcExperiment__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.insdcExperiment__describedBy, domain=None, range=Optional[str])

slots.insdcExperiment__schema_version = Slot(uri=HCA.schema_version, name="insdcExperiment__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.insdcExperiment__schema_version, domain=None, range=Optional[str])

slots.insdcExperiment__insdc_experiment_accession = Slot(uri=HCA.insdc_experiment_accession, name="insdcExperiment__insdc_experiment_accession", curie=HCA.curie('insdc_experiment_accession'),
                   model_uri=HCA.insdcExperiment__insdc_experiment_accession, domain=None, range=str)

slots.barcode__describedBy = Slot(uri=HCA.describedBy, name="barcode__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.barcode__describedBy, domain=None, range=Optional[str])

slots.barcode__schema_version = Slot(uri=HCA.schema_version, name="barcode__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.barcode__schema_version, domain=None, range=Optional[str])

slots.barcode__barcode_read = Slot(uri=HCA.barcode_read, name="barcode__barcode_read", curie=HCA.curie('barcode_read'),
                   model_uri=HCA.barcode__barcode_read, domain=None, range=Union[str, "BarcodeBarcodeReadOptions"])

slots.barcode__barcode_offset = Slot(uri=HCA.barcode_offset, name="barcode__barcode_offset", curie=HCA.curie('barcode_offset'),
                   model_uri=HCA.barcode__barcode_offset, domain=None, range=int)

slots.barcode__barcode_length = Slot(uri=HCA.barcode_length, name="barcode__barcode_length", curie=HCA.curie('barcode_length'),
                   model_uri=HCA.barcode__barcode_length, domain=None, range=int)

slots.barcode__white_list_file = Slot(uri=HCA.white_list_file, name="barcode__white_list_file", curie=HCA.curie('white_list_file'),
                   model_uri=HCA.barcode__white_list_file, domain=None, range=Optional[str])

slots.s10x__describedBy = Slot(uri=HCA.describedBy, name="s10x__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.s10x__describedBy, domain=None, range=Optional[str])

slots.s10x__schema_version = Slot(uri=HCA.schema_version, name="s10x__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.s10x__schema_version, domain=None, range=Optional[str])

slots.s10x__fastq_method = Slot(uri=HCA.fastq_method, name="s10x__fastq_method", curie=HCA.curie('fastq_method'),
                   model_uri=HCA.s10x__fastq_method, domain=None, range=Optional[str])

slots.s10x__fastq_method_version = Slot(uri=HCA.fastq_method_version, name="s10x__fastq_method_version", curie=HCA.curie('fastq_method_version'),
                   model_uri=HCA.s10x__fastq_method_version, domain=None, range=Optional[str])

slots.s10x__pooled_channels = Slot(uri=HCA.pooled_channels, name="s10x__pooled_channels", curie=HCA.curie('pooled_channels'),
                   model_uri=HCA.s10x__pooled_channels, domain=None, range=Optional[float])

slots.s10x__drop_uniformity = Slot(uri=HCA.drop_uniformity, name="s10x__drop_uniformity", curie=HCA.curie('drop_uniformity'),
                   model_uri=HCA.s10x__drop_uniformity, domain=None, range=Optional[Union[bool, Bool]])

slots.plateBasedSequencing__describedBy = Slot(uri=HCA.describedBy, name="plateBasedSequencing__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.plateBasedSequencing__describedBy, domain=None, range=Optional[str])

slots.plateBasedSequencing__schema_version = Slot(uri=HCA.schema_version, name="plateBasedSequencing__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.plateBasedSequencing__schema_version, domain=None, range=Optional[str])

slots.plateBasedSequencing__plate_label = Slot(uri=HCA.plate_label, name="plateBasedSequencing__plate_label", curie=HCA.curie('plate_label'),
                   model_uri=HCA.plateBasedSequencing__plate_label, domain=None, range=str)

slots.plateBasedSequencing__well_label = Slot(uri=HCA.well_label, name="plateBasedSequencing__well_label", curie=HCA.curie('well_label'),
                   model_uri=HCA.plateBasedSequencing__well_label, domain=None, range=Optional[str])

slots.plateBasedSequencing__well_quality = Slot(uri=HCA.well_quality, name="plateBasedSequencing__well_quality", curie=HCA.curie('well_quality'),
                   model_uri=HCA.plateBasedSequencing__well_quality, domain=None, range=Optional[Union[str, "PlateBasedSequencingWellQualityOptions"]])

slots.provenance__describedBy = Slot(uri=HCA.describedBy, name="provenance__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.provenance__describedBy, domain=None, range=Optional[str])

slots.provenance__schema_version = Slot(uri=HCA.schema_version, name="provenance__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.provenance__schema_version, domain=None, range=Optional[str])

slots.provenance__schema_major_version = Slot(uri=HCA.schema_major_version, name="provenance__schema_major_version", curie=HCA.curie('schema_major_version'),
                   model_uri=HCA.provenance__schema_major_version, domain=None, range=Optional[int])

slots.provenance__schema_minor_version = Slot(uri=HCA.schema_minor_version, name="provenance__schema_minor_version", curie=HCA.curie('schema_minor_version'),
                   model_uri=HCA.provenance__schema_minor_version, domain=None, range=Optional[int])

slots.provenance__submission_date = Slot(uri=HCA.submission_date, name="provenance__submission_date", curie=HCA.curie('submission_date'),
                   model_uri=HCA.provenance__submission_date, domain=None, range=str)

slots.provenance__submitter_id = Slot(uri=HCA.submitter_id, name="provenance__submitter_id", curie=HCA.curie('submitter_id'),
                   model_uri=HCA.provenance__submitter_id, domain=None, range=Optional[str])

slots.provenance__update_date = Slot(uri=HCA.update_date, name="provenance__update_date", curie=HCA.curie('update_date'),
                   model_uri=HCA.provenance__update_date, domain=None, range=Optional[str])

slots.provenance__updater_id = Slot(uri=HCA.updater_id, name="provenance__updater_id", curie=HCA.curie('updater_id'),
                   model_uri=HCA.provenance__updater_id, domain=None, range=Optional[str])

slots.provenance__document_id = Slot(uri=HCA.document_id, name="provenance__document_id", curie=HCA.curie('document_id'),
                   model_uri=HCA.provenance__document_id, domain=None, range=str)

slots.provenance__accession = Slot(uri=HCA.accession, name="provenance__accession", curie=HCA.curie('accession'),
                   model_uri=HCA.provenance__accession, domain=None, range=Optional[str])

slots.fileDescriptor__describedBy = Slot(uri=HCA.describedBy, name="fileDescriptor__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.fileDescriptor__describedBy, domain=None, range=str)

slots.fileDescriptor__schema_version = Slot(uri=HCA.schema_version, name="fileDescriptor__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.fileDescriptor__schema_version, domain=None, range=Optional[str])

slots.fileDescriptor__schema_type = Slot(uri=HCA.schema_type, name="fileDescriptor__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.fileDescriptor__schema_type, domain=None, range=Union[str, "FileDescriptorSchemaTypeOptions"])

slots.fileDescriptor__file_name = Slot(uri=HCA.file_name, name="fileDescriptor__file_name", curie=HCA.curie('file_name'),
                   model_uri=HCA.fileDescriptor__file_name, domain=None, range=str)

slots.fileDescriptor__file_id = Slot(uri=HCA.file_id, name="fileDescriptor__file_id", curie=HCA.curie('file_id'),
                   model_uri=HCA.fileDescriptor__file_id, domain=None, range=str)

slots.fileDescriptor__file_version = Slot(uri=HCA.file_version, name="fileDescriptor__file_version", curie=HCA.curie('file_version'),
                   model_uri=HCA.fileDescriptor__file_version, domain=None, range=str)

slots.fileDescriptor__content_type = Slot(uri=HCA.content_type, name="fileDescriptor__content_type", curie=HCA.curie('content_type'),
                   model_uri=HCA.fileDescriptor__content_type, domain=None, range=str)

slots.fileDescriptor__size = Slot(uri=HCA.size, name="fileDescriptor__size", curie=HCA.curie('size'),
                   model_uri=HCA.fileDescriptor__size, domain=None, range=int)

slots.fileDescriptor__sha256 = Slot(uri=HCA.sha256, name="fileDescriptor__sha256", curie=HCA.curie('sha256'),
                   model_uri=HCA.fileDescriptor__sha256, domain=None, range=str)

slots.fileDescriptor__crc32c = Slot(uri=HCA.crc32c, name="fileDescriptor__crc32c", curie=HCA.curie('crc32c'),
                   model_uri=HCA.fileDescriptor__crc32c, domain=None, range=str)

slots.fileDescriptor__sha1 = Slot(uri=HCA.sha1, name="fileDescriptor__sha1", curie=HCA.curie('sha1'),
                   model_uri=HCA.fileDescriptor__sha1, domain=None, range=Optional[str])

slots.fileDescriptor__s3_etag = Slot(uri=HCA.s3_etag, name="fileDescriptor__s3_etag", curie=HCA.curie('s3_etag'),
                   model_uri=HCA.fileDescriptor__s3_etag, domain=None, range=Optional[str])

slots.input__input_type = Slot(uri=HCA.input_type, name="input__input_type", curie=HCA.curie('input_type'),
                   model_uri=HCA.input__input_type, domain=None, range=str)

slots.input__input_id = Slot(uri=HCA.input_id, name="input__input_id", curie=HCA.curie('input_id'),
                   model_uri=HCA.input__input_id, domain=None, range=str)

slots.output__output_type = Slot(uri=HCA.output_type, name="output__output_type", curie=HCA.curie('output_type'),
                   model_uri=HCA.output__output_type, domain=None, range=str)

slots.output__output_id = Slot(uri=HCA.output_id, name="output__output_id", curie=HCA.curie('output_id'),
                   model_uri=HCA.output__output_id, domain=None, range=str)

slots.protocolReference__protocol_type = Slot(uri=HCA.protocol_type, name="protocolReference__protocol_type", curie=HCA.curie('protocol_type'),
                   model_uri=HCA.protocolReference__protocol_type, domain=None, range=Union[str, "ProtocolReferenceProtocolTypeOptions"])

slots.protocolReference__protocol_id = Slot(uri=HCA.protocol_id, name="protocolReference__protocol_id", curie=HCA.curie('protocol_id'),
                   model_uri=HCA.protocolReference__protocol_id, domain=None, range=str)

slots.processLink__process_type = Slot(uri=HCA.process_type, name="processLink__process_type", curie=HCA.curie('process_type'),
                   model_uri=HCA.processLink__process_type, domain=None, range=str)

slots.processLink__process_id = Slot(uri=HCA.process_id, name="processLink__process_id", curie=HCA.curie('process_id'),
                   model_uri=HCA.processLink__process_id, domain=None, range=str)

slots.processLink__inputs = Slot(uri=HCA.inputs, name="processLink__inputs", curie=HCA.curie('inputs'),
                   model_uri=HCA.processLink__inputs, domain=None, range=Union[Union[dict, Input], List[Union[dict, Input]]])

slots.processLink__outputs = Slot(uri=HCA.outputs, name="processLink__outputs", curie=HCA.curie('outputs'),
                   model_uri=HCA.processLink__outputs, domain=None, range=Union[Union[dict, Output], List[Union[dict, Output]]])

slots.processLink__protocols = Slot(uri=HCA.protocols, name="processLink__protocols", curie=HCA.curie('protocols'),
                   model_uri=HCA.processLink__protocols, domain=None, range=Union[Union[dict, ProtocolReference], List[Union[dict, ProtocolReference]]])

slots.processLink__link_type = Slot(uri=HCA.link_type, name="processLink__link_type", curie=HCA.curie('link_type'),
                   model_uri=HCA.processLink__link_type, domain=None, range=Union[str, "ProcessLinkLinkTypeOptions"])

slots.supplementaryFileEntity__file_id = Slot(uri=HCA.file_id, name="supplementaryFileEntity__file_id", curie=HCA.curie('file_id'),
                   model_uri=HCA.supplementaryFileEntity__file_id, domain=None, range=str)

slots.supplementaryFileEntity__file_type = Slot(uri=HCA.file_type, name="supplementaryFileEntity__file_type", curie=HCA.curie('file_type'),
                   model_uri=HCA.supplementaryFileEntity__file_type, domain=None, range=Union[str, "SupplementaryFileEntityFileTypeOptions"])

slots.entity__entity_id = Slot(uri=HCA.entity_id, name="entity__entity_id", curie=HCA.curie('entity_id'),
                   model_uri=HCA.entity__entity_id, domain=None, range=str)

slots.entity__entity_type = Slot(uri=HCA.entity_type, name="entity__entity_type", curie=HCA.curie('entity_type'),
                   model_uri=HCA.entity__entity_type, domain=None, range=Union[str, "EntityEntityTypeOptions"])

slots.supplementaryFileLink__entity = Slot(uri=HCA.entity, name="supplementaryFileLink__entity", curie=HCA.curie('entity'),
                   model_uri=HCA.supplementaryFileLink__entity, domain=None, range=Union[dict, Entity])

slots.supplementaryFileLink__files = Slot(uri=HCA.files, name="supplementaryFileLink__files", curie=HCA.curie('files'),
                   model_uri=HCA.supplementaryFileLink__files, domain=None, range=Union[Union[dict, SupplementaryFile], List[Union[dict, SupplementaryFile]]])

slots.supplementaryFileLink__link_type = Slot(uri=HCA.link_type, name="supplementaryFileLink__link_type", curie=HCA.curie('link_type'),
                   model_uri=HCA.supplementaryFileLink__link_type, domain=None, range=Union[str, "SupplementaryFileLinkLinkTypeOptions"])

slots.links__describedBy = Slot(uri=HCA.describedBy, name="links__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.links__describedBy, domain=None, range=str)

slots.links__schema_version = Slot(uri=HCA.schema_version, name="links__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.links__schema_version, domain=None, range=Optional[str])

slots.links__schema_type = Slot(uri=HCA.schema_type, name="links__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.links__schema_type, domain=None, range=Union[str, "LinksSchemaTypeOptions"])

slots.links__links = Slot(uri=HCA.links, name="links__links", curie=HCA.curie('links'),
                   model_uri=HCA.links__links, domain=None, range=Union[str, List[str]])

slots.license__describedBy = Slot(uri=HCA.describedBy, name="license__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.license__describedBy, domain=None, range=Optional[str])

slots.license__schema_version = Slot(uri=HCA.schema_version, name="license__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.license__schema_version, domain=None, range=Optional[str])

slots.license__identifier = Slot(uri=HCA.identifier, name="license__identifier", curie=HCA.curie('identifier'),
                   model_uri=HCA.license__identifier, domain=None, range=Optional[str])

slots.license__full_name = Slot(uri=HCA.full_name, name="license__full_name", curie=HCA.curie('full_name'),
                   model_uri=HCA.license__full_name, domain=None, range=Optional[str])

slots.license__url = Slot(uri=HCA.url, name="license__url", curie=HCA.curie('url'),
                   model_uri=HCA.license__url, domain=None, range=Optional[str])

slots.sequenceFile__describedBy = Slot(uri=HCA.describedBy, name="sequenceFile__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.sequenceFile__describedBy, domain=None, range=str)

slots.sequenceFile__schema_version = Slot(uri=HCA.schema_version, name="sequenceFile__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.sequenceFile__schema_version, domain=None, range=Optional[str])

slots.sequenceFile__schema_type = Slot(uri=HCA.schema_type, name="sequenceFile__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.sequenceFile__schema_type, domain=None, range=Union[str, "SequenceFileSchemaTypeOptions"])

slots.sequenceFile__provenance = Slot(uri=HCA.provenance, name="sequenceFile__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.sequenceFile__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.sequenceFile__file_core = Slot(uri=HCA.file_core, name="sequenceFile__file_core", curie=HCA.curie('file_core'),
                   model_uri=HCA.sequenceFile__file_core, domain=None, range=Union[dict, FileCore])

slots.sequenceFile__read_index = Slot(uri=HCA.read_index, name="sequenceFile__read_index", curie=HCA.curie('read_index'),
                   model_uri=HCA.sequenceFile__read_index, domain=None, range=Union[str, "SequenceFileReadIndexOptions"])

slots.sequenceFile__lane_index = Slot(uri=HCA.lane_index, name="sequenceFile__lane_index", curie=HCA.curie('lane_index'),
                   model_uri=HCA.sequenceFile__lane_index, domain=None, range=Optional[int])

slots.sequenceFile__read_length = Slot(uri=HCA.read_length, name="sequenceFile__read_length", curie=HCA.curie('read_length'),
                   model_uri=HCA.sequenceFile__read_length, domain=None, range=Optional[int])

slots.sequenceFile__insdc_run_accessions = Slot(uri=HCA.insdc_run_accessions, name="sequenceFile__insdc_run_accessions", curie=HCA.curie('insdc_run_accessions'),
                   model_uri=HCA.sequenceFile__insdc_run_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.sequenceFile__library_prep_id = Slot(uri=HCA.library_prep_id, name="sequenceFile__library_prep_id", curie=HCA.curie('library_prep_id'),
                   model_uri=HCA.sequenceFile__library_prep_id, domain=None, range=Optional[str])

slots.imageFile__describedBy = Slot(uri=HCA.describedBy, name="imageFile__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.imageFile__describedBy, domain=None, range=str)

slots.imageFile__schema_version = Slot(uri=HCA.schema_version, name="imageFile__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.imageFile__schema_version, domain=None, range=Optional[str])

slots.imageFile__schema_type = Slot(uri=HCA.schema_type, name="imageFile__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.imageFile__schema_type, domain=None, range=Union[str, "ImageFileSchemaTypeOptions"])

slots.imageFile__provenance = Slot(uri=HCA.provenance, name="imageFile__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.imageFile__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.imageFile__file_core = Slot(uri=HCA.file_core, name="imageFile__file_core", curie=HCA.curie('file_core'),
                   model_uri=HCA.imageFile__file_core, domain=None, range=Union[dict, FileCore])

slots.supplementaryFile__describedBy = Slot(uri=HCA.describedBy, name="supplementaryFile__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.supplementaryFile__describedBy, domain=None, range=str)

slots.supplementaryFile__schema_version = Slot(uri=HCA.schema_version, name="supplementaryFile__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.supplementaryFile__schema_version, domain=None, range=Optional[str])

slots.supplementaryFile__schema_type = Slot(uri=HCA.schema_type, name="supplementaryFile__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.supplementaryFile__schema_type, domain=None, range=Union[str, "SupplementaryFileSchemaTypeOptions"])

slots.supplementaryFile__provenance = Slot(uri=HCA.provenance, name="supplementaryFile__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.supplementaryFile__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.supplementaryFile__file_core = Slot(uri=HCA.file_core, name="supplementaryFile__file_core", curie=HCA.curie('file_core'),
                   model_uri=HCA.supplementaryFile__file_core, domain=None, range=Union[dict, FileCore])

slots.supplementaryFile__file_description = Slot(uri=HCA.file_description, name="supplementaryFile__file_description", curie=HCA.curie('file_description'),
                   model_uri=HCA.supplementaryFile__file_description, domain=None, range=Optional[str])

slots.analysisFile__describedBy = Slot(uri=HCA.describedBy, name="analysisFile__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.analysisFile__describedBy, domain=None, range=str)

slots.analysisFile__schema_version = Slot(uri=HCA.schema_version, name="analysisFile__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.analysisFile__schema_version, domain=None, range=Optional[str])

slots.analysisFile__schema_type = Slot(uri=HCA.schema_type, name="analysisFile__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.analysisFile__schema_type, domain=None, range=Union[str, "AnalysisFileSchemaTypeOptions"])

slots.analysisFile__provenance = Slot(uri=HCA.provenance, name="analysisFile__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.analysisFile__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.analysisFile__file_core = Slot(uri=HCA.file_core, name="analysisFile__file_core", curie=HCA.curie('file_core'),
                   model_uri=HCA.analysisFile__file_core, domain=None, range=Union[dict, FileCore])

slots.analysisFile__matrix_cell_count = Slot(uri=HCA.matrix_cell_count, name="analysisFile__matrix_cell_count", curie=HCA.curie('matrix_cell_count'),
                   model_uri=HCA.analysisFile__matrix_cell_count, domain=None, range=Optional[int])

slots.referenceFile__describedBy = Slot(uri=HCA.describedBy, name="referenceFile__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.referenceFile__describedBy, domain=None, range=str)

slots.referenceFile__schema_version = Slot(uri=HCA.schema_version, name="referenceFile__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.referenceFile__schema_version, domain=None, range=Optional[str])

slots.referenceFile__schema_type = Slot(uri=HCA.schema_type, name="referenceFile__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.referenceFile__schema_type, domain=None, range=Union[str, "ReferenceFileSchemaTypeOptions"])

slots.referenceFile__provenance = Slot(uri=HCA.provenance, name="referenceFile__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.referenceFile__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.referenceFile__file_core = Slot(uri=HCA.file_core, name="referenceFile__file_core", curie=HCA.curie('file_core'),
                   model_uri=HCA.referenceFile__file_core, domain=None, range=Union[dict, FileCore])

slots.referenceFile__ncbi_taxon_id = Slot(uri=HCA.ncbi_taxon_id, name="referenceFile__ncbi_taxon_id", curie=HCA.curie('ncbi_taxon_id'),
                   model_uri=HCA.referenceFile__ncbi_taxon_id, domain=None, range=int)

slots.referenceFile__genus_species = Slot(uri=HCA.genus_species, name="referenceFile__genus_species", curie=HCA.curie('genus_species'),
                   model_uri=HCA.referenceFile__genus_species, domain=None, range=Union[dict, SpeciesOntology])

slots.referenceFile__reference_type = Slot(uri=HCA.reference_type, name="referenceFile__reference_type", curie=HCA.curie('reference_type'),
                   model_uri=HCA.referenceFile__reference_type, domain=None, range=Union[str, "ReferenceFileReferenceTypeOptions"])

slots.referenceFile__assembly_type = Slot(uri=HCA.assembly_type, name="referenceFile__assembly_type", curie=HCA.curie('assembly_type'),
                   model_uri=HCA.referenceFile__assembly_type, domain=None, range=Union[str, "ReferenceFileAssemblyTypeOptions"])

slots.referenceFile__reference_version = Slot(uri=HCA.reference_version, name="referenceFile__reference_version", curie=HCA.curie('reference_version'),
                   model_uri=HCA.referenceFile__reference_version, domain=None, range=str)

slots.protocol__describedBy = Slot(uri=HCA.describedBy, name="protocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.protocol__describedBy, domain=None, range=str)

slots.protocol__schema_version = Slot(uri=HCA.schema_version, name="protocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.protocol__schema_version, domain=None, range=Optional[str])

slots.protocol__schema_type = Slot(uri=HCA.schema_type, name="protocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.protocol__schema_type, domain=None, range=Union[str, "ProtocolSchemaTypeOptions"])

slots.protocol__provenance = Slot(uri=HCA.provenance, name="protocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.protocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.protocol__protocol_core = Slot(uri=HCA.protocol_core, name="protocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.protocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.protocol__type = Slot(uri=HCA.type, name="protocol__type", curie=HCA.curie('type'),
                   model_uri=HCA.protocol__type, domain=None, range=Optional[Union[dict, ProcessTypeOntology]])

slots.sequencingProtocol__describedBy = Slot(uri=HCA.describedBy, name="sequencingProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.sequencingProtocol__describedBy, domain=None, range=str)

slots.sequencingProtocol__schema_version = Slot(uri=HCA.schema_version, name="sequencingProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.sequencingProtocol__schema_version, domain=None, range=Optional[str])

slots.sequencingProtocol__schema_type = Slot(uri=HCA.schema_type, name="sequencingProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.sequencingProtocol__schema_type, domain=None, range=Union[str, "SequencingProtocolSchemaTypeOptions"])

slots.sequencingProtocol__provenance = Slot(uri=HCA.provenance, name="sequencingProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.sequencingProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.sequencingProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="sequencingProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.sequencingProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.sequencingProtocol__instrument_manufacturer_model = Slot(uri=HCA.instrument_manufacturer_model, name="sequencingProtocol__instrument_manufacturer_model", curie=HCA.curie('instrument_manufacturer_model'),
                   model_uri=HCA.sequencingProtocol__instrument_manufacturer_model, domain=None, range=Union[dict, InstrumentOntology])

slots.sequencingProtocol__local_machine_name = Slot(uri=HCA.local_machine_name, name="sequencingProtocol__local_machine_name", curie=HCA.curie('local_machine_name'),
                   model_uri=HCA.sequencingProtocol__local_machine_name, domain=None, range=Optional[str])

slots.sequencingProtocol__paired_end = Slot(uri=HCA.paired_end, name="sequencingProtocol__paired_end", curie=HCA.curie('paired_end'),
                   model_uri=HCA.sequencingProtocol__paired_end, domain=None, range=Union[bool, Bool])

slots.sequencingProtocol__method = Slot(uri=HCA.method, name="sequencingProtocol__method", curie=HCA.curie('method'),
                   model_uri=HCA.sequencingProtocol__method, domain=None, range=Union[dict, SequencingOntology])

slots.sequencingProtocol__s10x = Slot(uri=HCA.s10x, name="sequencingProtocol__s10x", curie=HCA.curie('s10x'),
                   model_uri=HCA.sequencingProtocol__s10x, domain=None, range=Optional[Union[dict, S10x]])

slots.libraryPreparationProtocol__describedBy = Slot(uri=HCA.describedBy, name="libraryPreparationProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.libraryPreparationProtocol__describedBy, domain=None, range=str)

slots.libraryPreparationProtocol__schema_version = Slot(uri=HCA.schema_version, name="libraryPreparationProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.libraryPreparationProtocol__schema_version, domain=None, range=Optional[str])

slots.libraryPreparationProtocol__schema_type = Slot(uri=HCA.schema_type, name="libraryPreparationProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.libraryPreparationProtocol__schema_type, domain=None, range=Union[str, "LibraryPreparationProtocolSchemaTypeOptions"])

slots.libraryPreparationProtocol__provenance = Slot(uri=HCA.provenance, name="libraryPreparationProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.libraryPreparationProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.libraryPreparationProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="libraryPreparationProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.libraryPreparationProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.libraryPreparationProtocol__cell_barcode = Slot(uri=HCA.cell_barcode, name="libraryPreparationProtocol__cell_barcode", curie=HCA.curie('cell_barcode'),
                   model_uri=HCA.libraryPreparationProtocol__cell_barcode, domain=None, range=Optional[Union[dict, Barcode]])

slots.libraryPreparationProtocol__spatial_barcode = Slot(uri=HCA.spatial_barcode, name="libraryPreparationProtocol__spatial_barcode", curie=HCA.curie('spatial_barcode'),
                   model_uri=HCA.libraryPreparationProtocol__spatial_barcode, domain=None, range=Optional[Union[dict, Barcode]])

slots.libraryPreparationProtocol__input_nucleic_acid_molecule = Slot(uri=HCA.input_nucleic_acid_molecule, name="libraryPreparationProtocol__input_nucleic_acid_molecule", curie=HCA.curie('input_nucleic_acid_molecule'),
                   model_uri=HCA.libraryPreparationProtocol__input_nucleic_acid_molecule, domain=None, range=Union[dict, BiologicalMacromoleculeOntology])

slots.libraryPreparationProtocol__nucleic_acid_source = Slot(uri=HCA.nucleic_acid_source, name="libraryPreparationProtocol__nucleic_acid_source", curie=HCA.curie('nucleic_acid_source'),
                   model_uri=HCA.libraryPreparationProtocol__nucleic_acid_source, domain=None, range=Union[str, "LibraryPreparationProtocolNucleicAcidSourceOptions"])

slots.libraryPreparationProtocol__library_construction_method = Slot(uri=HCA.library_construction_method, name="libraryPreparationProtocol__library_construction_method", curie=HCA.curie('library_construction_method'),
                   model_uri=HCA.libraryPreparationProtocol__library_construction_method, domain=None, range=Union[dict, LibraryConstructionOntology])

slots.libraryPreparationProtocol__library_construction_kit = Slot(uri=HCA.library_construction_kit, name="libraryPreparationProtocol__library_construction_kit", curie=HCA.curie('library_construction_kit'),
                   model_uri=HCA.libraryPreparationProtocol__library_construction_kit, domain=None, range=Optional[Union[dict, PurchasedReagents]])

slots.libraryPreparationProtocol__nucleic_acid_conversion_kit = Slot(uri=HCA.nucleic_acid_conversion_kit, name="libraryPreparationProtocol__nucleic_acid_conversion_kit", curie=HCA.curie('nucleic_acid_conversion_kit'),
                   model_uri=HCA.libraryPreparationProtocol__nucleic_acid_conversion_kit, domain=None, range=Optional[Union[dict, PurchasedReagents]])

slots.libraryPreparationProtocol__end_bias = Slot(uri=HCA.end_bias, name="libraryPreparationProtocol__end_bias", curie=HCA.curie('end_bias'),
                   model_uri=HCA.libraryPreparationProtocol__end_bias, domain=None, range=Union[str, "LibraryPreparationProtocolEndBiasOptions"])

slots.libraryPreparationProtocol__primer = Slot(uri=HCA.primer, name="libraryPreparationProtocol__primer", curie=HCA.curie('primer'),
                   model_uri=HCA.libraryPreparationProtocol__primer, domain=None, range=Optional[Union[str, "LibraryPreparationProtocolPrimerOptions"]])

slots.libraryPreparationProtocol__strand = Slot(uri=HCA.strand, name="libraryPreparationProtocol__strand", curie=HCA.curie('strand'),
                   model_uri=HCA.libraryPreparationProtocol__strand, domain=None, range=Union[str, "LibraryPreparationProtocolStrandOptions"])

slots.libraryPreparationProtocol__spike_in_kit = Slot(uri=HCA.spike_in_kit, name="libraryPreparationProtocol__spike_in_kit", curie=HCA.curie('spike_in_kit'),
                   model_uri=HCA.libraryPreparationProtocol__spike_in_kit, domain=None, range=Optional[Union[dict, PurchasedReagents]])

slots.libraryPreparationProtocol__spike_in_dilution = Slot(uri=HCA.spike_in_dilution, name="libraryPreparationProtocol__spike_in_dilution", curie=HCA.curie('spike_in_dilution'),
                   model_uri=HCA.libraryPreparationProtocol__spike_in_dilution, domain=None, range=Optional[int])

slots.libraryPreparationProtocol__umi_barcode = Slot(uri=HCA.umi_barcode, name="libraryPreparationProtocol__umi_barcode", curie=HCA.curie('umi_barcode'),
                   model_uri=HCA.libraryPreparationProtocol__umi_barcode, domain=None, range=Optional[Union[dict, Barcode]])

slots.libraryPreparationProtocol__library_preamplification_method = Slot(uri=HCA.library_preamplification_method, name="libraryPreparationProtocol__library_preamplification_method", curie=HCA.curie('library_preamplification_method'),
                   model_uri=HCA.libraryPreparationProtocol__library_preamplification_method, domain=None, range=Optional[Union[dict, LibraryAmplificationOntology]])

slots.libraryPreparationProtocol__cdna_library_amplification_method = Slot(uri=HCA.cdna_library_amplification_method, name="libraryPreparationProtocol__cdna_library_amplification_method", curie=HCA.curie('cdna_library_amplification_method'),
                   model_uri=HCA.libraryPreparationProtocol__cdna_library_amplification_method, domain=None, range=Optional[Union[dict, LibraryAmplificationOntology]])

slots.libraryPreparationProtocol__nominal_length = Slot(uri=HCA.nominal_length, name="libraryPreparationProtocol__nominal_length", curie=HCA.curie('nominal_length'),
                   model_uri=HCA.libraryPreparationProtocol__nominal_length, domain=None, range=Optional[int])

slots.libraryPreparationProtocol__nominal_sdev = Slot(uri=HCA.nominal_sdev, name="libraryPreparationProtocol__nominal_sdev", curie=HCA.curie('nominal_sdev'),
                   model_uri=HCA.libraryPreparationProtocol__nominal_sdev, domain=None, range=Optional[int])

slots.analysisProtocol__describedBy = Slot(uri=HCA.describedBy, name="analysisProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.analysisProtocol__describedBy, domain=None, range=str)

slots.analysisProtocol__schema_version = Slot(uri=HCA.schema_version, name="analysisProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.analysisProtocol__schema_version, domain=None, range=Optional[str])

slots.analysisProtocol__schema_type = Slot(uri=HCA.schema_type, name="analysisProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.analysisProtocol__schema_type, domain=None, range=Union[str, "AnalysisProtocolSchemaTypeOptions"])

slots.analysisProtocol__provenance = Slot(uri=HCA.provenance, name="analysisProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.analysisProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.analysisProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="analysisProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.analysisProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.analysisProtocol__type = Slot(uri=HCA.type, name="analysisProtocol__type", curie=HCA.curie('type'),
                   model_uri=HCA.analysisProtocol__type, domain=None, range=Union[dict, ProcessTypeOntology])

slots.analysisProtocol__computational_method = Slot(uri=HCA.computational_method, name="analysisProtocol__computational_method", curie=HCA.curie('computational_method'),
                   model_uri=HCA.analysisProtocol__computational_method, domain=None, range=Optional[str])

slots.analysisProtocol__matrix = Slot(uri=HCA.matrix, name="analysisProtocol__matrix", curie=HCA.curie('matrix'),
                   model_uri=HCA.analysisProtocol__matrix, domain=None, range=Optional[Union[dict, Matrix]])

slots.aggregateGenerationProtocol__describedBy = Slot(uri=HCA.describedBy, name="aggregateGenerationProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.aggregateGenerationProtocol__describedBy, domain=None, range=str)

slots.aggregateGenerationProtocol__schema_version = Slot(uri=HCA.schema_version, name="aggregateGenerationProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.aggregateGenerationProtocol__schema_version, domain=None, range=Optional[str])

slots.aggregateGenerationProtocol__schema_type = Slot(uri=HCA.schema_type, name="aggregateGenerationProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.aggregateGenerationProtocol__schema_type, domain=None, range=Union[str, "AggregateGenerationProtocolSchemaTypeOptions"])

slots.aggregateGenerationProtocol__provenance = Slot(uri=HCA.provenance, name="aggregateGenerationProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.aggregateGenerationProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.aggregateGenerationProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="aggregateGenerationProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.aggregateGenerationProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.aggregateGenerationProtocol__formation_method = Slot(uri=HCA.formation_method, name="aggregateGenerationProtocol__formation_method", curie=HCA.curie('formation_method'),
                   model_uri=HCA.aggregateGenerationProtocol__formation_method, domain=None, range=str)

slots.aggregateGenerationProtocol__cell_uniformity = Slot(uri=HCA.cell_uniformity, name="aggregateGenerationProtocol__cell_uniformity", curie=HCA.curie('cell_uniformity'),
                   model_uri=HCA.aggregateGenerationProtocol__cell_uniformity, domain=None, range=Optional[str])

slots.enrichmentProtocol__describedBy = Slot(uri=HCA.describedBy, name="enrichmentProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.enrichmentProtocol__describedBy, domain=None, range=str)

slots.enrichmentProtocol__schema_version = Slot(uri=HCA.schema_version, name="enrichmentProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.enrichmentProtocol__schema_version, domain=None, range=Optional[str])

slots.enrichmentProtocol__schema_type = Slot(uri=HCA.schema_type, name="enrichmentProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.enrichmentProtocol__schema_type, domain=None, range=Union[str, "EnrichmentProtocolSchemaTypeOptions"])

slots.enrichmentProtocol__provenance = Slot(uri=HCA.provenance, name="enrichmentProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.enrichmentProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.enrichmentProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="enrichmentProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.enrichmentProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.enrichmentProtocol__method = Slot(uri=HCA.method, name="enrichmentProtocol__method", curie=HCA.curie('method'),
                   model_uri=HCA.enrichmentProtocol__method, domain=None, range=Union[dict, ProcessTypeOntology])

slots.enrichmentProtocol__markers = Slot(uri=HCA.markers, name="enrichmentProtocol__markers", curie=HCA.curie('markers'),
                   model_uri=HCA.enrichmentProtocol__markers, domain=None, range=Optional[str])

slots.enrichmentProtocol__minimum_size = Slot(uri=HCA.minimum_size, name="enrichmentProtocol__minimum_size", curie=HCA.curie('minimum_size'),
                   model_uri=HCA.enrichmentProtocol__minimum_size, domain=None, range=Optional[float])

slots.enrichmentProtocol__maximum_size = Slot(uri=HCA.maximum_size, name="enrichmentProtocol__maximum_size", curie=HCA.curie('maximum_size'),
                   model_uri=HCA.enrichmentProtocol__maximum_size, domain=None, range=Optional[float])

slots.dissociationProtocol__describedBy = Slot(uri=HCA.describedBy, name="dissociationProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.dissociationProtocol__describedBy, domain=None, range=str)

slots.dissociationProtocol__schema_version = Slot(uri=HCA.schema_version, name="dissociationProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.dissociationProtocol__schema_version, domain=None, range=Optional[str])

slots.dissociationProtocol__schema_type = Slot(uri=HCA.schema_type, name="dissociationProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.dissociationProtocol__schema_type, domain=None, range=Union[str, "DissociationProtocolSchemaTypeOptions"])

slots.dissociationProtocol__provenance = Slot(uri=HCA.provenance, name="dissociationProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.dissociationProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.dissociationProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="dissociationProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.dissociationProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.dissociationProtocol__method = Slot(uri=HCA.method, name="dissociationProtocol__method", curie=HCA.curie('method'),
                   model_uri=HCA.dissociationProtocol__method, domain=None, range=Union[dict, ProcessTypeOntology])

slots.dissociationProtocol__reagents = Slot(uri=HCA.reagents, name="dissociationProtocol__reagents", curie=HCA.curie('reagents'),
                   model_uri=HCA.dissociationProtocol__reagents, domain=None, range=Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]])

slots.ipscInductionProtocol__describedBy = Slot(uri=HCA.describedBy, name="ipscInductionProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.ipscInductionProtocol__describedBy, domain=None, range=str)

slots.ipscInductionProtocol__schema_version = Slot(uri=HCA.schema_version, name="ipscInductionProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.ipscInductionProtocol__schema_version, domain=None, range=Optional[str])

slots.ipscInductionProtocol__schema_type = Slot(uri=HCA.schema_type, name="ipscInductionProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.ipscInductionProtocol__schema_type, domain=None, range=Union[str, "IpscInductionProtocolSchemaTypeOptions"])

slots.ipscInductionProtocol__provenance = Slot(uri=HCA.provenance, name="ipscInductionProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.ipscInductionProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.ipscInductionProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="ipscInductionProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.ipscInductionProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.ipscInductionProtocol__method = Slot(uri=HCA.method, name="ipscInductionProtocol__method", curie=HCA.curie('method'),
                   model_uri=HCA.ipscInductionProtocol__method, domain=None, range=Union[str, "IpscInductionProtocolMethodOptions"])

slots.ipscInductionProtocol__reprogramming_factors = Slot(uri=HCA.reprogramming_factors, name="ipscInductionProtocol__reprogramming_factors", curie=HCA.curie('reprogramming_factors'),
                   model_uri=HCA.ipscInductionProtocol__reprogramming_factors, domain=None, range=Optional[str])

slots.ipscInductionProtocol__ipsc_induction_kit = Slot(uri=HCA.ipsc_induction_kit, name="ipscInductionProtocol__ipsc_induction_kit", curie=HCA.curie('ipsc_induction_kit'),
                   model_uri=HCA.ipscInductionProtocol__ipsc_induction_kit, domain=None, range=Optional[Union[dict, PurchasedReagents]])

slots.ipscInductionProtocol__pluripotency_test = Slot(uri=HCA.pluripotency_test, name="ipscInductionProtocol__pluripotency_test", curie=HCA.curie('pluripotency_test'),
                   model_uri=HCA.ipscInductionProtocol__pluripotency_test, domain=None, range=Optional[str])

slots.ipscInductionProtocol__percent_pluripotency = Slot(uri=HCA.percent_pluripotency, name="ipscInductionProtocol__percent_pluripotency", curie=HCA.curie('percent_pluripotency'),
                   model_uri=HCA.ipscInductionProtocol__percent_pluripotency, domain=None, range=Optional[float])

slots.ipscInductionProtocol__pluripotency_vector_removed = Slot(uri=HCA.pluripotency_vector_removed, name="ipscInductionProtocol__pluripotency_vector_removed", curie=HCA.curie('pluripotency_vector_removed'),
                   model_uri=HCA.ipscInductionProtocol__pluripotency_vector_removed, domain=None, range=Optional[Union[str, "IpscInductionProtocolPluripotencyVectorRemovedOptions"]])

slots.ipscInductionProtocol__reagents = Slot(uri=HCA.reagents, name="ipscInductionProtocol__reagents", curie=HCA.curie('reagents'),
                   model_uri=HCA.ipscInductionProtocol__reagents, domain=None, range=Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]])

slots.collectionProtocol__describedBy = Slot(uri=HCA.describedBy, name="collectionProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.collectionProtocol__describedBy, domain=None, range=str)

slots.collectionProtocol__schema_version = Slot(uri=HCA.schema_version, name="collectionProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.collectionProtocol__schema_version, domain=None, range=Optional[str])

slots.collectionProtocol__schema_type = Slot(uri=HCA.schema_type, name="collectionProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.collectionProtocol__schema_type, domain=None, range=Union[str, "CollectionProtocolSchemaTypeOptions"])

slots.collectionProtocol__provenance = Slot(uri=HCA.provenance, name="collectionProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.collectionProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.collectionProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="collectionProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.collectionProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.collectionProtocol__method = Slot(uri=HCA.method, name="collectionProtocol__method", curie=HCA.curie('method'),
                   model_uri=HCA.collectionProtocol__method, domain=None, range=Union[dict, ProcessTypeOntology])

slots.collectionProtocol__reagents = Slot(uri=HCA.reagents, name="collectionProtocol__reagents", curie=HCA.curie('reagents'),
                   model_uri=HCA.collectionProtocol__reagents, domain=None, range=Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]])

slots.differentiationProtocol__describedBy = Slot(uri=HCA.describedBy, name="differentiationProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.differentiationProtocol__describedBy, domain=None, range=str)

slots.differentiationProtocol__schema_version = Slot(uri=HCA.schema_version, name="differentiationProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.differentiationProtocol__schema_version, domain=None, range=Optional[str])

slots.differentiationProtocol__schema_type = Slot(uri=HCA.schema_type, name="differentiationProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.differentiationProtocol__schema_type, domain=None, range=Union[str, "DifferentiationProtocolSchemaTypeOptions"])

slots.differentiationProtocol__provenance = Slot(uri=HCA.provenance, name="differentiationProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.differentiationProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.differentiationProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="differentiationProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.differentiationProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.differentiationProtocol__method = Slot(uri=HCA.method, name="differentiationProtocol__method", curie=HCA.curie('method'),
                   model_uri=HCA.differentiationProtocol__method, domain=None, range=str)

slots.differentiationProtocol__media = Slot(uri=HCA.media, name="differentiationProtocol__media", curie=HCA.curie('media'),
                   model_uri=HCA.differentiationProtocol__media, domain=None, range=Optional[str])

slots.differentiationProtocol__small_molecules = Slot(uri=HCA.small_molecules, name="differentiationProtocol__small_molecules", curie=HCA.curie('small_molecules'),
                   model_uri=HCA.differentiationProtocol__small_molecules, domain=None, range=Optional[str])

slots.differentiationProtocol__target_cell_yield = Slot(uri=HCA.target_cell_yield, name="differentiationProtocol__target_cell_yield", curie=HCA.curie('target_cell_yield'),
                   model_uri=HCA.differentiationProtocol__target_cell_yield, domain=None, range=Optional[float])

slots.differentiationProtocol__reagents = Slot(uri=HCA.reagents, name="differentiationProtocol__reagents", curie=HCA.curie('reagents'),
                   model_uri=HCA.differentiationProtocol__reagents, domain=None, range=Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]])

slots.differentiationProtocol__target_pathway = Slot(uri=HCA.target_pathway, name="differentiationProtocol__target_pathway", curie=HCA.curie('target_pathway'),
                   model_uri=HCA.differentiationProtocol__target_pathway, domain=None, range=Optional[str])

slots.differentiationProtocol__validation_method = Slot(uri=HCA.validation_method, name="differentiationProtocol__validation_method", curie=HCA.curie('validation_method'),
                   model_uri=HCA.differentiationProtocol__validation_method, domain=None, range=Optional[str])

slots.differentiationProtocol__validation_result = Slot(uri=HCA.validation_result, name="differentiationProtocol__validation_result", curie=HCA.curie('validation_result'),
                   model_uri=HCA.differentiationProtocol__validation_result, domain=None, range=Optional[str])

slots.treatmentProtocol__describedBy = Slot(uri=HCA.describedBy, name="treatmentProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.treatmentProtocol__describedBy, domain=None, range=str)

slots.treatmentProtocol__schema_version = Slot(uri=HCA.schema_version, name="treatmentProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.treatmentProtocol__schema_version, domain=None, range=Optional[str])

slots.treatmentProtocol__schema_type = Slot(uri=HCA.schema_type, name="treatmentProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.treatmentProtocol__schema_type, domain=None, range=Union[str, "TreatmentProtocolSchemaTypeOptions"])

slots.treatmentProtocol__provenance = Slot(uri=HCA.provenance, name="treatmentProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.treatmentProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.treatmentProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="treatmentProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.treatmentProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.treatmentProtocol__method = Slot(uri=HCA.method, name="treatmentProtocol__method", curie=HCA.curie('method'),
                   model_uri=HCA.treatmentProtocol__method, domain=None, range=Union[Union[dict, TreatmentMethodOntology], List[Union[dict, TreatmentMethodOntology]]])

slots.treatmentProtocol__media = Slot(uri=HCA.media, name="treatmentProtocol__media", curie=HCA.curie('media'),
                   model_uri=HCA.treatmentProtocol__media, domain=None, range=Optional[str])

slots.treatmentProtocol__reagents = Slot(uri=HCA.reagents, name="treatmentProtocol__reagents", curie=HCA.curie('reagents'),
                   model_uri=HCA.treatmentProtocol__reagents, domain=None, range=Optional[Union[Union[dict, PurchasedReagents], List[Union[dict, PurchasedReagents]]]])

slots.treatmentProtocol__target_pathway = Slot(uri=HCA.target_pathway, name="treatmentProtocol__target_pathway", curie=HCA.curie('target_pathway'),
                   model_uri=HCA.treatmentProtocol__target_pathway, domain=None, range=Optional[Union[Union[dict, TargetPathwayOntology], List[Union[dict, TargetPathwayOntology]]]])

slots.imagingPreparationProtocol__describedBy = Slot(uri=HCA.describedBy, name="imagingPreparationProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.imagingPreparationProtocol__describedBy, domain=None, range=str)

slots.imagingPreparationProtocol__schema_version = Slot(uri=HCA.schema_version, name="imagingPreparationProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.imagingPreparationProtocol__schema_version, domain=None, range=Optional[str])

slots.imagingPreparationProtocol__schema_type = Slot(uri=HCA.schema_type, name="imagingPreparationProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.imagingPreparationProtocol__schema_type, domain=None, range=Union[str, "ImagingPreparationProtocolSchemaTypeOptions"])

slots.imagingPreparationProtocol__provenance = Slot(uri=HCA.provenance, name="imagingPreparationProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.imagingPreparationProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.imagingPreparationProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="imagingPreparationProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.imagingPreparationProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.imagingPreparationProtocol__fresh_slicing_method = Slot(uri=HCA.fresh_slicing_method, name="imagingPreparationProtocol__fresh_slicing_method", curie=HCA.curie('fresh_slicing_method'),
                   model_uri=HCA.imagingPreparationProtocol__fresh_slicing_method, domain=None, range=Optional[str])

slots.imagingPreparationProtocol__imaged_slice_thickness = Slot(uri=HCA.imaged_slice_thickness, name="imagingPreparationProtocol__imaged_slice_thickness", curie=HCA.curie('imaged_slice_thickness'),
                   model_uri=HCA.imagingPreparationProtocol__imaged_slice_thickness, domain=None, range=Optional[float])

slots.imagingPreparationProtocol__final_slicing_method = Slot(uri=HCA.final_slicing_method, name="imagingPreparationProtocol__final_slicing_method", curie=HCA.curie('final_slicing_method'),
                   model_uri=HCA.imagingPreparationProtocol__final_slicing_method, domain=None, range=Optional[str])

slots.imagingPreparationProtocol__post_resection_interval = Slot(uri=HCA.post_resection_interval, name="imagingPreparationProtocol__post_resection_interval", curie=HCA.curie('post_resection_interval'),
                   model_uri=HCA.imagingPreparationProtocol__post_resection_interval, domain=None, range=Optional[float])

slots.imagingPreparationProtocol__post_resection_interval_unit = Slot(uri=HCA.post_resection_interval_unit, name="imagingPreparationProtocol__post_resection_interval_unit", curie=HCA.curie('post_resection_interval_unit'),
                   model_uri=HCA.imagingPreparationProtocol__post_resection_interval_unit, domain=None, range=Optional[Union[dict, TimeUnitOntology]])

slots.imagingPreparationProtocol__pre_final_slice_preservation_method = Slot(uri=HCA.pre_final_slice_preservation_method, name="imagingPreparationProtocol__pre_final_slice_preservation_method", curie=HCA.curie('pre_final_slice_preservation_method'),
                   model_uri=HCA.imagingPreparationProtocol__pre_final_slice_preservation_method, domain=None, range=Optional[Union[dict, PreservationStorage]])

slots.imagingPreparationProtocol__post_final_slicing_interval = Slot(uri=HCA.post_final_slicing_interval, name="imagingPreparationProtocol__post_final_slicing_interval", curie=HCA.curie('post_final_slicing_interval'),
                   model_uri=HCA.imagingPreparationProtocol__post_final_slicing_interval, domain=None, range=Optional[float])

slots.imagingPreparationProtocol__post_final_slicing_interval_unit = Slot(uri=HCA.post_final_slicing_interval_unit, name="imagingPreparationProtocol__post_final_slicing_interval_unit", curie=HCA.curie('post_final_slicing_interval_unit'),
                   model_uri=HCA.imagingPreparationProtocol__post_final_slicing_interval_unit, domain=None, range=Optional[Union[dict, TimeUnitOntology]])

slots.imagingPreparationProtocol__fiducial_marker = Slot(uri=HCA.fiducial_marker, name="imagingPreparationProtocol__fiducial_marker", curie=HCA.curie('fiducial_marker'),
                   model_uri=HCA.imagingPreparationProtocol__fiducial_marker, domain=None, range=Optional[str])

slots.imagingPreparationProtocol__expansion_factor = Slot(uri=HCA.expansion_factor, name="imagingPreparationProtocol__expansion_factor", curie=HCA.curie('expansion_factor'),
                   model_uri=HCA.imagingPreparationProtocol__expansion_factor, domain=None, range=Optional[float])

slots.imagingPreparationProtocol__permeabilisation_time = Slot(uri=HCA.permeabilisation_time, name="imagingPreparationProtocol__permeabilisation_time", curie=HCA.curie('permeabilisation_time'),
                   model_uri=HCA.imagingPreparationProtocol__permeabilisation_time, domain=None, range=Optional[float])

slots.imagingPreparationProtocol__permeabilisation_time_unit = Slot(uri=HCA.permeabilisation_time_unit, name="imagingPreparationProtocol__permeabilisation_time_unit", curie=HCA.curie('permeabilisation_time_unit'),
                   model_uri=HCA.imagingPreparationProtocol__permeabilisation_time_unit, domain=None, range=Optional[Union[dict, TimeUnitOntology]])

slots.imagingProtocol__describedBy = Slot(uri=HCA.describedBy, name="imagingProtocol__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.imagingProtocol__describedBy, domain=None, range=str)

slots.imagingProtocol__schema_version = Slot(uri=HCA.schema_version, name="imagingProtocol__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.imagingProtocol__schema_version, domain=None, range=Optional[str])

slots.imagingProtocol__schema_type = Slot(uri=HCA.schema_type, name="imagingProtocol__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.imagingProtocol__schema_type, domain=None, range=Union[str, "ImagingProtocolSchemaTypeOptions"])

slots.imagingProtocol__provenance = Slot(uri=HCA.provenance, name="imagingProtocol__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.imagingProtocol__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.imagingProtocol__protocol_core = Slot(uri=HCA.protocol_core, name="imagingProtocol__protocol_core", curie=HCA.curie('protocol_core'),
                   model_uri=HCA.imagingProtocol__protocol_core, domain=None, range=Union[dict, ProtocolCore])

slots.imagingProtocol__microscope_setup_description = Slot(uri=HCA.microscope_setup_description, name="imagingProtocol__microscope_setup_description", curie=HCA.curie('microscope_setup_description'),
                   model_uri=HCA.imagingProtocol__microscope_setup_description, domain=None, range=Optional[str])

slots.imagingProtocol__microscopy_technique = Slot(uri=HCA.microscopy_technique, name="imagingProtocol__microscopy_technique", curie=HCA.curie('microscopy_technique'),
                   model_uri=HCA.imagingProtocol__microscopy_technique, domain=None, range=Union[dict, MicroscopyOntology])

slots.imagingProtocol__magnification = Slot(uri=HCA.magnification, name="imagingProtocol__magnification", curie=HCA.curie('magnification'),
                   model_uri=HCA.imagingProtocol__magnification, domain=None, range=str)

slots.imagingProtocol__numerical_aperture = Slot(uri=HCA.numerical_aperture, name="imagingProtocol__numerical_aperture", curie=HCA.curie('numerical_aperture'),
                   model_uri=HCA.imagingProtocol__numerical_aperture, domain=None, range=Optional[float])

slots.imagingProtocol__immersion_medium_type = Slot(uri=HCA.immersion_medium_type, name="imagingProtocol__immersion_medium_type", curie=HCA.curie('immersion_medium_type'),
                   model_uri=HCA.imagingProtocol__immersion_medium_type, domain=None, range=Optional[str])

slots.imagingProtocol__immersion_medium_refractive_index = Slot(uri=HCA.immersion_medium_refractive_index, name="imagingProtocol__immersion_medium_refractive_index", curie=HCA.curie('immersion_medium_refractive_index'),
                   model_uri=HCA.imagingProtocol__immersion_medium_refractive_index, domain=None, range=Optional[float])

slots.imagingProtocol__pixel_size = Slot(uri=HCA.pixel_size, name="imagingProtocol__pixel_size", curie=HCA.curie('pixel_size'),
                   model_uri=HCA.imagingProtocol__pixel_size, domain=None, range=Optional[float])

slots.imagingProtocol__number_of_tiles = Slot(uri=HCA.number_of_tiles, name="imagingProtocol__number_of_tiles", curie=HCA.curie('number_of_tiles'),
                   model_uri=HCA.imagingProtocol__number_of_tiles, domain=None, range=Optional[int])

slots.imagingProtocol__tile_size_y = Slot(uri=HCA.tile_size_y, name="imagingProtocol__tile_size_y", curie=HCA.curie('tile_size_y'),
                   model_uri=HCA.imagingProtocol__tile_size_y, domain=None, range=Optional[float])

slots.imagingProtocol__tile_size_x = Slot(uri=HCA.tile_size_x, name="imagingProtocol__tile_size_x", curie=HCA.curie('tile_size_x'),
                   model_uri=HCA.imagingProtocol__tile_size_x, domain=None, range=Optional[float])

slots.imagingProtocol__z_stack_step_size = Slot(uri=HCA.z_stack_step_size, name="imagingProtocol__z_stack_step_size", curie=HCA.curie('z_stack_step_size'),
                   model_uri=HCA.imagingProtocol__z_stack_step_size, domain=None, range=Optional[float])

slots.imagingProtocol__number_of_z_steps = Slot(uri=HCA.number_of_z_steps, name="imagingProtocol__number_of_z_steps", curie=HCA.curie('number_of_z_steps'),
                   model_uri=HCA.imagingProtocol__number_of_z_steps, domain=None, range=Optional[int])

slots.imagingProtocol__overlapping_tiles = Slot(uri=HCA.overlapping_tiles, name="imagingProtocol__overlapping_tiles", curie=HCA.curie('overlapping_tiles'),
                   model_uri=HCA.imagingProtocol__overlapping_tiles, domain=None, range=Optional[Union[str, "ImagingProtocolOverlappingTilesOptions"]])

slots.imagingProtocol__channel = Slot(uri=HCA.channel, name="imagingProtocol__channel", curie=HCA.curie('channel'),
                   model_uri=HCA.imagingProtocol__channel, domain=None, range=Optional[Union[Union[dict, Channel], List[Union[dict, Channel]]]])

slots.imagingProtocol__probe = Slot(uri=HCA.probe, name="imagingProtocol__probe", curie=HCA.curie('probe'),
                   model_uri=HCA.imagingProtocol__probe, domain=None, range=Optional[Union[Union[dict, Probe], List[Union[dict, Probe]]]])

slots.project__describedBy = Slot(uri=HCA.describedBy, name="project__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.project__describedBy, domain=None, range=str)

slots.project__schema_version = Slot(uri=HCA.schema_version, name="project__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.project__schema_version, domain=None, range=Optional[str])

slots.project__schema_type = Slot(uri=HCA.schema_type, name="project__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.project__schema_type, domain=None, range=Union[str, "ProjectSchemaTypeOptions"])

slots.project__provenance = Slot(uri=HCA.provenance, name="project__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.project__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.project__project_core = Slot(uri=HCA.project_core, name="project__project_core", curie=HCA.curie('project_core'),
                   model_uri=HCA.project__project_core, domain=None, range=Union[dict, ProjectCore])

slots.project__contributors = Slot(uri=HCA.contributors, name="project__contributors", curie=HCA.curie('contributors'),
                   model_uri=HCA.project__contributors, domain=None, range=Optional[Union[Union[dict, Contact], List[Union[dict, Contact]]]])

slots.project__supplementary_links = Slot(uri=HCA.supplementary_links, name="project__supplementary_links", curie=HCA.curie('supplementary_links'),
                   model_uri=HCA.project__supplementary_links, domain=None, range=Optional[Union[str, List[str]]])

slots.project__publications = Slot(uri=HCA.publications, name="project__publications", curie=HCA.curie('publications'),
                   model_uri=HCA.project__publications, domain=None, range=Optional[Union[Union[dict, Publication], List[Union[dict, Publication]]]])

slots.project__insdc_project_accessions = Slot(uri=HCA.insdc_project_accessions, name="project__insdc_project_accessions", curie=HCA.curie('insdc_project_accessions'),
                   model_uri=HCA.project__insdc_project_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.project__ega_accessions = Slot(uri=HCA.ega_accessions, name="project__ega_accessions", curie=HCA.curie('ega_accessions'),
                   model_uri=HCA.project__ega_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.project__dbgap_accessions = Slot(uri=HCA.dbgap_accessions, name="project__dbgap_accessions", curie=HCA.curie('dbgap_accessions'),
                   model_uri=HCA.project__dbgap_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.project__geo_series_accessions = Slot(uri=HCA.geo_series_accessions, name="project__geo_series_accessions", curie=HCA.curie('geo_series_accessions'),
                   model_uri=HCA.project__geo_series_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.project__array_express_accessions = Slot(uri=HCA.array_express_accessions, name="project__array_express_accessions", curie=HCA.curie('array_express_accessions'),
                   model_uri=HCA.project__array_express_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.project__insdc_study_accessions = Slot(uri=HCA.insdc_study_accessions, name="project__insdc_study_accessions", curie=HCA.curie('insdc_study_accessions'),
                   model_uri=HCA.project__insdc_study_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.project__biostudies_accessions = Slot(uri=HCA.biostudies_accessions, name="project__biostudies_accessions", curie=HCA.curie('biostudies_accessions'),
                   model_uri=HCA.project__biostudies_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.project__funders = Slot(uri=HCA.funders, name="project__funders", curie=HCA.curie('funders'),
                   model_uri=HCA.project__funders, domain=None, range=Union[Union[dict, Funder], List[Union[dict, Funder]]])

slots.project__estimated_cell_count = Slot(uri=HCA.estimated_cell_count, name="project__estimated_cell_count", curie=HCA.curie('estimated_cell_count'),
                   model_uri=HCA.project__estimated_cell_count, domain=None, range=Optional[int])

slots.specimenFromOrganism__describedBy = Slot(uri=HCA.describedBy, name="specimenFromOrganism__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.specimenFromOrganism__describedBy, domain=None, range=str)

slots.specimenFromOrganism__schema_version = Slot(uri=HCA.schema_version, name="specimenFromOrganism__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.specimenFromOrganism__schema_version, domain=None, range=Optional[str])

slots.specimenFromOrganism__schema_type = Slot(uri=HCA.schema_type, name="specimenFromOrganism__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.specimenFromOrganism__schema_type, domain=None, range=Union[str, "SpecimenFromOrganismSchemaTypeOptions"])

slots.specimenFromOrganism__provenance = Slot(uri=HCA.provenance, name="specimenFromOrganism__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.specimenFromOrganism__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.specimenFromOrganism__biomaterial_core = Slot(uri=HCA.biomaterial_core, name="specimenFromOrganism__biomaterial_core", curie=HCA.curie('biomaterial_core'),
                   model_uri=HCA.specimenFromOrganism__biomaterial_core, domain=None, range=Union[dict, BiomaterialCore])

slots.specimenFromOrganism__genus_species = Slot(uri=HCA.genus_species, name="specimenFromOrganism__genus_species", curie=HCA.curie('genus_species'),
                   model_uri=HCA.specimenFromOrganism__genus_species, domain=None, range=Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]])

slots.specimenFromOrganism__organ = Slot(uri=HCA.organ, name="specimenFromOrganism__organ", curie=HCA.curie('organ'),
                   model_uri=HCA.specimenFromOrganism__organ, domain=None, range=Union[dict, OrganOntology])

slots.specimenFromOrganism__organ_parts = Slot(uri=HCA.organ_parts, name="specimenFromOrganism__organ_parts", curie=HCA.curie('organ_parts'),
                   model_uri=HCA.specimenFromOrganism__organ_parts, domain=None, range=Optional[Union[Union[dict, OrganPartOntology], List[Union[dict, OrganPartOntology]]]])

slots.specimenFromOrganism__diseases = Slot(uri=HCA.diseases, name="specimenFromOrganism__diseases", curie=HCA.curie('diseases'),
                   model_uri=HCA.specimenFromOrganism__diseases, domain=None, range=Optional[Union[Union[dict, DiseaseOntology], List[Union[dict, DiseaseOntology]]]])

slots.specimenFromOrganism__state_of_specimen = Slot(uri=HCA.state_of_specimen, name="specimenFromOrganism__state_of_specimen", curie=HCA.curie('state_of_specimen'),
                   model_uri=HCA.specimenFromOrganism__state_of_specimen, domain=None, range=Optional[Union[dict, StateOfSpecimen]])

slots.specimenFromOrganism__preservation_storage = Slot(uri=HCA.preservation_storage, name="specimenFromOrganism__preservation_storage", curie=HCA.curie('preservation_storage'),
                   model_uri=HCA.specimenFromOrganism__preservation_storage, domain=None, range=Optional[Union[dict, PreservationStorage]])

slots.specimenFromOrganism__collection_time = Slot(uri=HCA.collection_time, name="specimenFromOrganism__collection_time", curie=HCA.curie('collection_time'),
                   model_uri=HCA.specimenFromOrganism__collection_time, domain=None, range=Optional[str])

slots.specimenFromOrganism__purchased_specimen = Slot(uri=HCA.purchased_specimen, name="specimenFromOrganism__purchased_specimen", curie=HCA.curie('purchased_specimen'),
                   model_uri=HCA.specimenFromOrganism__purchased_specimen, domain=None, range=Optional[Union[dict, PurchasedReagents]])

slots.cellSuspension__describedBy = Slot(uri=HCA.describedBy, name="cellSuspension__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.cellSuspension__describedBy, domain=None, range=str)

slots.cellSuspension__schema_version = Slot(uri=HCA.schema_version, name="cellSuspension__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.cellSuspension__schema_version, domain=None, range=Optional[str])

slots.cellSuspension__schema_type = Slot(uri=HCA.schema_type, name="cellSuspension__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.cellSuspension__schema_type, domain=None, range=Union[str, "CellSuspensionSchemaTypeOptions"])

slots.cellSuspension__provenance = Slot(uri=HCA.provenance, name="cellSuspension__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.cellSuspension__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.cellSuspension__biomaterial_core = Slot(uri=HCA.biomaterial_core, name="cellSuspension__biomaterial_core", curie=HCA.curie('biomaterial_core'),
                   model_uri=HCA.cellSuspension__biomaterial_core, domain=None, range=Union[dict, BiomaterialCore])

slots.cellSuspension__cell_morphology = Slot(uri=HCA.cell_morphology, name="cellSuspension__cell_morphology", curie=HCA.curie('cell_morphology'),
                   model_uri=HCA.cellSuspension__cell_morphology, domain=None, range=Optional[Union[dict, CellMorphology]])

slots.cellSuspension__growth_conditions = Slot(uri=HCA.growth_conditions, name="cellSuspension__growth_conditions", curie=HCA.curie('growth_conditions'),
                   model_uri=HCA.cellSuspension__growth_conditions, domain=None, range=Optional[Union[dict, GrowthConditions]])

slots.cellSuspension__genus_species = Slot(uri=HCA.genus_species, name="cellSuspension__genus_species", curie=HCA.curie('genus_species'),
                   model_uri=HCA.cellSuspension__genus_species, domain=None, range=Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]])

slots.cellSuspension__selected_cell_types = Slot(uri=HCA.selected_cell_types, name="cellSuspension__selected_cell_types", curie=HCA.curie('selected_cell_types'),
                   model_uri=HCA.cellSuspension__selected_cell_types, domain=None, range=Optional[Union[Union[dict, CellTypeOntology], List[Union[dict, CellTypeOntology]]]])

slots.cellSuspension__estimated_cell_count = Slot(uri=HCA.estimated_cell_count, name="cellSuspension__estimated_cell_count", curie=HCA.curie('estimated_cell_count'),
                   model_uri=HCA.cellSuspension__estimated_cell_count, domain=None, range=Optional[int])

slots.cellSuspension__plate_based_sequencing = Slot(uri=HCA.plate_based_sequencing, name="cellSuspension__plate_based_sequencing", curie=HCA.curie('plate_based_sequencing'),
                   model_uri=HCA.cellSuspension__plate_based_sequencing, domain=None, range=Optional[Union[dict, PlateBasedSequencing]])

slots.cellSuspension__timecourse = Slot(uri=HCA.timecourse, name="cellSuspension__timecourse", curie=HCA.curie('timecourse'),
                   model_uri=HCA.cellSuspension__timecourse, domain=None, range=Optional[Union[dict, Timecourse]])

slots.cellLine__describedBy = Slot(uri=HCA.describedBy, name="cellLine__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.cellLine__describedBy, domain=None, range=str)

slots.cellLine__schema_version = Slot(uri=HCA.schema_version, name="cellLine__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.cellLine__schema_version, domain=None, range=Optional[str])

slots.cellLine__schema_type = Slot(uri=HCA.schema_type, name="cellLine__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.cellLine__schema_type, domain=None, range=Union[str, "CellLineSchemaTypeOptions"])

slots.cellLine__provenance = Slot(uri=HCA.provenance, name="cellLine__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.cellLine__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.cellLine__biomaterial_core = Slot(uri=HCA.biomaterial_core, name="cellLine__biomaterial_core", curie=HCA.curie('biomaterial_core'),
                   model_uri=HCA.cellLine__biomaterial_core, domain=None, range=Union[dict, BiomaterialCore])

slots.cellLine__supplier = Slot(uri=HCA.supplier, name="cellLine__supplier", curie=HCA.curie('supplier'),
                   model_uri=HCA.cellLine__supplier, domain=None, range=Optional[str])

slots.cellLine__catalog_number = Slot(uri=HCA.catalog_number, name="cellLine__catalog_number", curie=HCA.curie('catalog_number'),
                   model_uri=HCA.cellLine__catalog_number, domain=None, range=Optional[str])

slots.cellLine__lot_number = Slot(uri=HCA.lot_number, name="cellLine__lot_number", curie=HCA.curie('lot_number'),
                   model_uri=HCA.cellLine__lot_number, domain=None, range=Optional[str])

slots.cellLine__catalog_url = Slot(uri=HCA.catalog_url, name="cellLine__catalog_url", curie=HCA.curie('catalog_url'),
                   model_uri=HCA.cellLine__catalog_url, domain=None, range=Optional[str])

slots.cellLine__cell_cycle = Slot(uri=HCA.cell_cycle, name="cellLine__cell_cycle", curie=HCA.curie('cell_cycle'),
                   model_uri=HCA.cellLine__cell_cycle, domain=None, range=Optional[Union[dict, CellCycleOntology]])

slots.cellLine__type = Slot(uri=HCA.type, name="cellLine__type", curie=HCA.curie('type'),
                   model_uri=HCA.cellLine__type, domain=None, range=Union[str, "CellLineTypeOptions"])

slots.cellLine__model_organ = Slot(uri=HCA.model_organ, name="cellLine__model_organ", curie=HCA.curie('model_organ'),
                   model_uri=HCA.cellLine__model_organ, domain=None, range=Union[dict, OrganOntology])

slots.cellLine__cell_morphology = Slot(uri=HCA.cell_morphology, name="cellLine__cell_morphology", curie=HCA.curie('cell_morphology'),
                   model_uri=HCA.cellLine__cell_morphology, domain=None, range=Optional[Union[dict, CellMorphology]])

slots.cellLine__growth_conditions = Slot(uri=HCA.growth_conditions, name="cellLine__growth_conditions", curie=HCA.curie('growth_conditions'),
                   model_uri=HCA.cellLine__growth_conditions, domain=None, range=Optional[Union[dict, GrowthConditions]])

slots.cellLine__confluency = Slot(uri=HCA.confluency, name="cellLine__confluency", curie=HCA.curie('confluency'),
                   model_uri=HCA.cellLine__confluency, domain=None, range=Optional[float])

slots.cellLine__cell_type = Slot(uri=HCA.cell_type, name="cellLine__cell_type", curie=HCA.curie('cell_type'),
                   model_uri=HCA.cellLine__cell_type, domain=None, range=Optional[Union[dict, CellTypeOntology]])

slots.cellLine__karyotype = Slot(uri=HCA.karyotype, name="cellLine__karyotype", curie=HCA.curie('karyotype'),
                   model_uri=HCA.cellLine__karyotype, domain=None, range=Optional[str])

slots.cellLine__tissue = Slot(uri=HCA.tissue, name="cellLine__tissue", curie=HCA.curie('tissue'),
                   model_uri=HCA.cellLine__tissue, domain=None, range=Optional[Union[dict, OrganPartOntology]])

slots.cellLine__date_established = Slot(uri=HCA.date_established, name="cellLine__date_established", curie=HCA.curie('date_established'),
                   model_uri=HCA.cellLine__date_established, domain=None, range=Optional[str])

slots.cellLine__disease = Slot(uri=HCA.disease, name="cellLine__disease", curie=HCA.curie('disease'),
                   model_uri=HCA.cellLine__disease, domain=None, range=Optional[Union[dict, DiseaseOntology]])

slots.cellLine__genus_species = Slot(uri=HCA.genus_species, name="cellLine__genus_species", curie=HCA.curie('genus_species'),
                   model_uri=HCA.cellLine__genus_species, domain=None, range=Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]])

slots.cellLine__publication = Slot(uri=HCA.publication, name="cellLine__publication", curie=HCA.curie('publication'),
                   model_uri=HCA.cellLine__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.cellLine__timecourse = Slot(uri=HCA.timecourse, name="cellLine__timecourse", curie=HCA.curie('timecourse'),
                   model_uri=HCA.cellLine__timecourse, domain=None, range=Optional[Union[dict, Timecourse]])

slots.imagedSpecimen__describedBy = Slot(uri=HCA.describedBy, name="imagedSpecimen__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.imagedSpecimen__describedBy, domain=None, range=str)

slots.imagedSpecimen__schema_version = Slot(uri=HCA.schema_version, name="imagedSpecimen__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.imagedSpecimen__schema_version, domain=None, range=Optional[str])

slots.imagedSpecimen__schema_type = Slot(uri=HCA.schema_type, name="imagedSpecimen__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.imagedSpecimen__schema_type, domain=None, range=Union[str, "ImagedSpecimenSchemaTypeOptions"])

slots.imagedSpecimen__provenance = Slot(uri=HCA.provenance, name="imagedSpecimen__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.imagedSpecimen__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.imagedSpecimen__biomaterial_core = Slot(uri=HCA.biomaterial_core, name="imagedSpecimen__biomaterial_core", curie=HCA.curie('biomaterial_core'),
                   model_uri=HCA.imagedSpecimen__biomaterial_core, domain=None, range=Union[dict, BiomaterialCore])

slots.imagedSpecimen__overview_images = Slot(uri=HCA.overview_images, name="imagedSpecimen__overview_images", curie=HCA.curie('overview_images'),
                   model_uri=HCA.imagedSpecimen__overview_images, domain=None, range=Optional[Union[str, List[str]]])

slots.imagedSpecimen__slice_thickness = Slot(uri=HCA.slice_thickness, name="imagedSpecimen__slice_thickness", curie=HCA.curie('slice_thickness'),
                   model_uri=HCA.imagedSpecimen__slice_thickness, domain=None, range=float)

slots.imagedSpecimen__internal_anatomical_structures = Slot(uri=HCA.internal_anatomical_structures, name="imagedSpecimen__internal_anatomical_structures", curie=HCA.curie('internal_anatomical_structures'),
                   model_uri=HCA.imagedSpecimen__internal_anatomical_structures, domain=None, range=Optional[Union[Union[dict, OrganPartOntology], List[Union[dict, OrganPartOntology]]]])

slots.donorOrganism__describedBy = Slot(uri=HCA.describedBy, name="donorOrganism__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.donorOrganism__describedBy, domain=None, range=str)

slots.donorOrganism__schema_version = Slot(uri=HCA.schema_version, name="donorOrganism__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.donorOrganism__schema_version, domain=None, range=Optional[str])

slots.donorOrganism__schema_type = Slot(uri=HCA.schema_type, name="donorOrganism__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.donorOrganism__schema_type, domain=None, range=Union[str, "DonorOrganismSchemaTypeOptions"])

slots.donorOrganism__provenance = Slot(uri=HCA.provenance, name="donorOrganism__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.donorOrganism__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.donorOrganism__biomaterial_core = Slot(uri=HCA.biomaterial_core, name="donorOrganism__biomaterial_core", curie=HCA.curie('biomaterial_core'),
                   model_uri=HCA.donorOrganism__biomaterial_core, domain=None, range=Union[dict, BiomaterialCore])

slots.donorOrganism__human_specific = Slot(uri=HCA.human_specific, name="donorOrganism__human_specific", curie=HCA.curie('human_specific'),
                   model_uri=HCA.donorOrganism__human_specific, domain=None, range=Optional[Union[dict, HumanSpecific]])

slots.donorOrganism__mouse_specific = Slot(uri=HCA.mouse_specific, name="donorOrganism__mouse_specific", curie=HCA.curie('mouse_specific'),
                   model_uri=HCA.donorOrganism__mouse_specific, domain=None, range=Optional[Union[dict, MouseSpecific]])

slots.donorOrganism__genus_species = Slot(uri=HCA.genus_species, name="donorOrganism__genus_species", curie=HCA.curie('genus_species'),
                   model_uri=HCA.donorOrganism__genus_species, domain=None, range=Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]])

slots.donorOrganism__sex = Slot(uri=HCA.sex, name="donorOrganism__sex", curie=HCA.curie('sex'),
                   model_uri=HCA.donorOrganism__sex, domain=None, range=Union[str, "DonorOrganismSexOptions"])

slots.donorOrganism__is_living = Slot(uri=HCA.is_living, name="donorOrganism__is_living", curie=HCA.curie('is_living'),
                   model_uri=HCA.donorOrganism__is_living, domain=None, range=Union[str, "DonorOrganismIsLivingOptions"])

slots.donorOrganism__organism_age = Slot(uri=HCA.organism_age, name="donorOrganism__organism_age", curie=HCA.curie('organism_age'),
                   model_uri=HCA.donorOrganism__organism_age, domain=None, range=Optional[str])

slots.donorOrganism__organism_age_unit = Slot(uri=HCA.organism_age_unit, name="donorOrganism__organism_age_unit", curie=HCA.curie('organism_age_unit'),
                   model_uri=HCA.donorOrganism__organism_age_unit, domain=None, range=Optional[Union[dict, TimeUnitOntology]])

slots.donorOrganism__development_stage = Slot(uri=HCA.development_stage, name="donorOrganism__development_stage", curie=HCA.curie('development_stage'),
                   model_uri=HCA.donorOrganism__development_stage, domain=None, range=Union[dict, DevelopmentStageOntology])

slots.donorOrganism__diseases = Slot(uri=HCA.diseases, name="donorOrganism__diseases", curie=HCA.curie('diseases'),
                   model_uri=HCA.donorOrganism__diseases, domain=None, range=Optional[Union[Union[dict, DiseaseOntology], List[Union[dict, DiseaseOntology]]]])

slots.donorOrganism__death = Slot(uri=HCA.death, name="donorOrganism__death", curie=HCA.curie('death'),
                   model_uri=HCA.donorOrganism__death, domain=None, range=Optional[Union[dict, Death]])

slots.donorOrganism__familial_relationships = Slot(uri=HCA.familial_relationships, name="donorOrganism__familial_relationships", curie=HCA.curie('familial_relationships'),
                   model_uri=HCA.donorOrganism__familial_relationships, domain=None, range=Optional[Union[Union[dict, FamilialRelationship], List[Union[dict, FamilialRelationship]]]])

slots.donorOrganism__medical_history = Slot(uri=HCA.medical_history, name="donorOrganism__medical_history", curie=HCA.curie('medical_history'),
                   model_uri=HCA.donorOrganism__medical_history, domain=None, range=Optional[Union[dict, MedicalHistory]])

slots.donorOrganism__gestational_age = Slot(uri=HCA.gestational_age, name="donorOrganism__gestational_age", curie=HCA.curie('gestational_age'),
                   model_uri=HCA.donorOrganism__gestational_age, domain=None, range=Optional[str])

slots.donorOrganism__gestational_age_unit = Slot(uri=HCA.gestational_age_unit, name="donorOrganism__gestational_age_unit", curie=HCA.curie('gestational_age_unit'),
                   model_uri=HCA.donorOrganism__gestational_age_unit, domain=None, range=Optional[Union[dict, TimeUnitOntology]])

slots.donorOrganism__height = Slot(uri=HCA.height, name="donorOrganism__height", curie=HCA.curie('height'),
                   model_uri=HCA.donorOrganism__height, domain=None, range=Optional[str])

slots.donorOrganism__height_unit = Slot(uri=HCA.height_unit, name="donorOrganism__height_unit", curie=HCA.curie('height_unit'),
                   model_uri=HCA.donorOrganism__height_unit, domain=None, range=Optional[Union[dict, LengthUnitOntology]])

slots.donorOrganism__weight = Slot(uri=HCA.weight, name="donorOrganism__weight", curie=HCA.curie('weight'),
                   model_uri=HCA.donorOrganism__weight, domain=None, range=Optional[str])

slots.donorOrganism__weight_unit = Slot(uri=HCA.weight_unit, name="donorOrganism__weight_unit", curie=HCA.curie('weight_unit'),
                   model_uri=HCA.donorOrganism__weight_unit, domain=None, range=Optional[Union[dict, MassUnitOntology]])

slots.donorOrganism__timecourse = Slot(uri=HCA.timecourse, name="donorOrganism__timecourse", curie=HCA.curie('timecourse'),
                   model_uri=HCA.donorOrganism__timecourse, domain=None, range=Optional[Union[dict, Timecourse]])

slots.organoid__describedBy = Slot(uri=HCA.describedBy, name="organoid__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.organoid__describedBy, domain=None, range=str)

slots.organoid__schema_version = Slot(uri=HCA.schema_version, name="organoid__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.organoid__schema_version, domain=None, range=Optional[str])

slots.organoid__schema_type = Slot(uri=HCA.schema_type, name="organoid__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.organoid__schema_type, domain=None, range=Union[str, "OrganoidSchemaTypeOptions"])

slots.organoid__provenance = Slot(uri=HCA.provenance, name="organoid__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.organoid__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.organoid__biomaterial_core = Slot(uri=HCA.biomaterial_core, name="organoid__biomaterial_core", curie=HCA.curie('biomaterial_core'),
                   model_uri=HCA.organoid__biomaterial_core, domain=None, range=Union[dict, BiomaterialCore])

slots.organoid__genus_species = Slot(uri=HCA.genus_species, name="organoid__genus_species", curie=HCA.curie('genus_species'),
                   model_uri=HCA.organoid__genus_species, domain=None, range=Optional[Union[Union[dict, SpeciesOntology], List[Union[dict, SpeciesOntology]]]])

slots.organoid__model_organ = Slot(uri=HCA.model_organ, name="organoid__model_organ", curie=HCA.curie('model_organ'),
                   model_uri=HCA.organoid__model_organ, domain=None, range=Union[dict, OrganOntology])

slots.organoid__model_organ_part = Slot(uri=HCA.model_organ_part, name="organoid__model_organ_part", curie=HCA.curie('model_organ_part'),
                   model_uri=HCA.organoid__model_organ_part, domain=None, range=Optional[Union[dict, OrganPartOntology]])

slots.organoid__age = Slot(uri=HCA.age, name="organoid__age", curie=HCA.curie('age'),
                   model_uri=HCA.organoid__age, domain=None, range=Optional[float])

slots.organoid__age_unit = Slot(uri=HCA.age_unit, name="organoid__age_unit", curie=HCA.curie('age_unit'),
                   model_uri=HCA.organoid__age_unit, domain=None, range=Optional[Union[dict, TimeUnitOntology]])

slots.organoid__size = Slot(uri=HCA.size, name="organoid__size", curie=HCA.curie('size'),
                   model_uri=HCA.organoid__size, domain=None, range=Optional[float])

slots.organoid__size_unit = Slot(uri=HCA.size_unit, name="organoid__size_unit", curie=HCA.curie('size_unit'),
                   model_uri=HCA.organoid__size_unit, domain=None, range=Optional[Union[dict, LengthUnitOntology]])

slots.organoid__morphology = Slot(uri=HCA.morphology, name="organoid__morphology", curie=HCA.curie('morphology'),
                   model_uri=HCA.organoid__morphology, domain=None, range=Optional[str])

slots.organoid__embedded_in_matrigel = Slot(uri=HCA.embedded_in_matrigel, name="organoid__embedded_in_matrigel", curie=HCA.curie('embedded_in_matrigel'),
                   model_uri=HCA.organoid__embedded_in_matrigel, domain=None, range=Optional[Union[bool, Bool]])

slots.organoid__growth_environment = Slot(uri=HCA.growth_environment, name="organoid__growth_environment", curie=HCA.curie('growth_environment'),
                   model_uri=HCA.organoid__growth_environment, domain=None, range=Optional[str])

slots.organoid__input_aggregate_cell_count = Slot(uri=HCA.input_aggregate_cell_count, name="organoid__input_aggregate_cell_count", curie=HCA.curie('input_aggregate_cell_count'),
                   model_uri=HCA.organoid__input_aggregate_cell_count, domain=None, range=Optional[float])

slots.organoid__stored_oxygen_levels = Slot(uri=HCA.stored_oxygen_levels, name="organoid__stored_oxygen_levels", curie=HCA.curie('stored_oxygen_levels'),
                   model_uri=HCA.organoid__stored_oxygen_levels, domain=None, range=Optional[float])

slots.process__describedBy = Slot(uri=HCA.describedBy, name="process__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.process__describedBy, domain=None, range=str)

slots.process__schema_version = Slot(uri=HCA.schema_version, name="process__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.process__schema_version, domain=None, range=Optional[str])

slots.process__schema_type = Slot(uri=HCA.schema_type, name="process__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.process__schema_type, domain=None, range=Union[str, "ProcessSchemaTypeOptions"])

slots.process__provenance = Slot(uri=HCA.provenance, name="process__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.process__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.process__process_core = Slot(uri=HCA.process_core, name="process__process_core", curie=HCA.curie('process_core'),
                   model_uri=HCA.process__process_core, domain=None, range=Union[dict, ProcessCore])

slots.process__start_time = Slot(uri=HCA.start_time, name="process__start_time", curie=HCA.curie('start_time'),
                   model_uri=HCA.process__start_time, domain=None, range=Optional[str])

slots.process__end_time = Slot(uri=HCA.end_time, name="process__end_time", curie=HCA.curie('end_time'),
                   model_uri=HCA.process__end_time, domain=None, range=Optional[str])

slots.process__length_of_time = Slot(uri=HCA.length_of_time, name="process__length_of_time", curie=HCA.curie('length_of_time'),
                   model_uri=HCA.process__length_of_time, domain=None, range=Optional[str])

slots.process__length_of_time_unit = Slot(uri=HCA.length_of_time_unit, name="process__length_of_time_unit", curie=HCA.curie('length_of_time_unit'),
                   model_uri=HCA.process__length_of_time_unit, domain=None, range=Optional[Union[dict, TimeUnitOntology]])

slots.process__type = Slot(uri=HCA.type, name="process__type", curie=HCA.curie('type'),
                   model_uri=HCA.process__type, domain=None, range=Optional[Union[dict, ProcessTypeOntology]])

slots.process__deviation_from_protocol = Slot(uri=HCA.deviation_from_protocol, name="process__deviation_from_protocol", curie=HCA.curie('deviation_from_protocol'),
                   model_uri=HCA.process__deviation_from_protocol, domain=None, range=Optional[str])

slots.process__insdc_experiment = Slot(uri=HCA.insdc_experiment, name="process__insdc_experiment", curie=HCA.curie('insdc_experiment'),
                   model_uri=HCA.process__insdc_experiment, domain=None, range=Optional[Union[dict, InsdcExperiment]])

slots.task__disk_size = Slot(uri=HCA.disk_size, name="task__disk_size", curie=HCA.curie('disk_size'),
                   model_uri=HCA.task__disk_size, domain=None, range=str)

slots.task__task_name = Slot(uri=HCA.task_name, name="task__task_name", curie=HCA.curie('task_name'),
                   model_uri=HCA.task__task_name, domain=None, range=str)

slots.task__zone = Slot(uri=HCA.zone, name="task__zone", curie=HCA.curie('zone'),
                   model_uri=HCA.task__zone, domain=None, range=str)

slots.task__log_err = Slot(uri=HCA.log_err, name="task__log_err", curie=HCA.curie('log_err'),
                   model_uri=HCA.task__log_err, domain=None, range=Optional[str])

slots.task__start_time = Slot(uri=HCA.start_time, name="task__start_time", curie=HCA.curie('start_time'),
                   model_uri=HCA.task__start_time, domain=None, range=str)

slots.task__cpus = Slot(uri=HCA.cpus, name="task__cpus", curie=HCA.curie('cpus'),
                   model_uri=HCA.task__cpus, domain=None, range=int)

slots.task__log_out = Slot(uri=HCA.log_out, name="task__log_out", curie=HCA.curie('log_out'),
                   model_uri=HCA.task__log_out, domain=None, range=Optional[str])

slots.task__stop_time = Slot(uri=HCA.stop_time, name="task__stop_time", curie=HCA.curie('stop_time'),
                   model_uri=HCA.task__stop_time, domain=None, range=str)

slots.task__memory = Slot(uri=HCA.memory, name="task__memory", curie=HCA.curie('memory'),
                   model_uri=HCA.task__memory, domain=None, range=str)

slots.task__docker_image = Slot(uri=HCA.docker_image, name="task__docker_image", curie=HCA.curie('docker_image'),
                   model_uri=HCA.task__docker_image, domain=None, range=str)

slots.parameter__checksum = Slot(uri=HCA.checksum, name="parameter__checksum", curie=HCA.curie('checksum'),
                   model_uri=HCA.parameter__checksum, domain=None, range=Optional[str])

slots.parameter__parameter_name = Slot(uri=HCA.parameter_name, name="parameter__parameter_name", curie=HCA.curie('parameter_name'),
                   model_uri=HCA.parameter__parameter_name, domain=None, range=str)

slots.parameter__parameter_value = Slot(uri=HCA.parameter_value, name="parameter__parameter_value", curie=HCA.curie('parameter_value'),
                   model_uri=HCA.parameter__parameter_value, domain=None, range=str)

slots.analysisProcess__describedBy = Slot(uri=HCA.describedBy, name="analysisProcess__describedBy", curie=HCA.curie('describedBy'),
                   model_uri=HCA.analysisProcess__describedBy, domain=None, range=str)

slots.analysisProcess__schema_version = Slot(uri=HCA.schema_version, name="analysisProcess__schema_version", curie=HCA.curie('schema_version'),
                   model_uri=HCA.analysisProcess__schema_version, domain=None, range=Optional[str])

slots.analysisProcess__schema_type = Slot(uri=HCA.schema_type, name="analysisProcess__schema_type", curie=HCA.curie('schema_type'),
                   model_uri=HCA.analysisProcess__schema_type, domain=None, range=Union[str, "AnalysisProcessSchemaTypeOptions"])

slots.analysisProcess__provenance = Slot(uri=HCA.provenance, name="analysisProcess__provenance", curie=HCA.curie('provenance'),
                   model_uri=HCA.analysisProcess__provenance, domain=None, range=Optional[Union[dict, Provenance]])

slots.analysisProcess__process_core = Slot(uri=HCA.process_core, name="analysisProcess__process_core", curie=HCA.curie('process_core'),
                   model_uri=HCA.analysisProcess__process_core, domain=None, range=Union[dict, ProcessCore])

slots.analysisProcess__type = Slot(uri=HCA.type, name="analysisProcess__type", curie=HCA.curie('type'),
                   model_uri=HCA.analysisProcess__type, domain=None, range=Union[dict, ProcessTypeOntology])

slots.analysisProcess__inputs = Slot(uri=HCA.inputs, name="analysisProcess__inputs", curie=HCA.curie('inputs'),
                   model_uri=HCA.analysisProcess__inputs, domain=None, range=Union[Union[dict, Parameter], List[Union[dict, Parameter]]])

slots.analysisProcess__tasks = Slot(uri=HCA.tasks, name="analysisProcess__tasks", curie=HCA.curie('tasks'),
                   model_uri=HCA.analysisProcess__tasks, domain=None, range=Union[Union[dict, Task], List[Union[dict, Task]]])

slots.analysisProcess__timestamp_start_utc = Slot(uri=HCA.timestamp_start_utc, name="analysisProcess__timestamp_start_utc", curie=HCA.curie('timestamp_start_utc'),
                   model_uri=HCA.analysisProcess__timestamp_start_utc, domain=None, range=str)

slots.analysisProcess__timestamp_stop_utc = Slot(uri=HCA.timestamp_stop_utc, name="analysisProcess__timestamp_stop_utc", curie=HCA.curie('timestamp_stop_utc'),
                   model_uri=HCA.analysisProcess__timestamp_stop_utc, domain=None, range=str)

slots.analysisProcess__analysis_run_type = Slot(uri=HCA.analysis_run_type, name="analysisProcess__analysis_run_type", curie=HCA.curie('analysis_run_type'),
                   model_uri=HCA.analysisProcess__analysis_run_type, domain=None, range=Union[str, "AnalysisProcessAnalysisRunTypeOptions"])

slots.analysisProcess__reference_files = Slot(uri=HCA.reference_files, name="analysisProcess__reference_files", curie=HCA.curie('reference_files'),
                   model_uri=HCA.analysisProcess__reference_files, domain=None, range=Union[str, List[str]])