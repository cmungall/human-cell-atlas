

CREATE TABLE "AggregateGenerationProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	formation_method TEXT NOT NULL, 
	cell_uniformity TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, formation_method, cell_uniformity)
);

CREATE TABLE "AnalysisFile" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(4) NOT NULL, 
	provenance TEXT, 
	file_core TEXT NOT NULL, 
	matrix_cell_count INTEGER, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, file_core, matrix_cell_count)
);

CREATE TABLE "AnalysisProcess" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(7) NOT NULL, 
	provenance TEXT, 
	process_core TEXT NOT NULL, 
	type TEXT NOT NULL, 
	inputs TEXT NOT NULL, 
	tasks TEXT NOT NULL, 
	timestamp_start_utc TEXT NOT NULL, 
	timestamp_stop_utc TEXT NOT NULL, 
	analysis_run_type VARCHAR(12) NOT NULL, 
	reference_files TEXT NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, process_core, type, inputs, tasks, timestamp_start_utc, timestamp_stop_utc, analysis_run_type, reference_files)
);

CREATE TABLE "AnalysisProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	type TEXT NOT NULL, 
	computational_method TEXT, 
	matrix TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, type, computational_method, matrix)
);

CREATE TABLE "Barcode" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	barcode_read VARCHAR(8) NOT NULL, 
	barcode_offset INTEGER NOT NULL, 
	barcode_length INTEGER NOT NULL, 
	white_list_file TEXT, 
	PRIMARY KEY ("describedBy", schema_version, barcode_read, barcode_offset, barcode_length, white_list_file)
);

CREATE TABLE "BiologicalMacromoleculeOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "BiomaterialCore" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	biomaterial_id TEXT NOT NULL, 
	biomaterial_name TEXT, 
	biomaterial_description TEXT, 
	ncbi_taxon_id INTEGER NOT NULL, 
	genotype TEXT, 
	supplementary_files TEXT, 
	biosamples_accession TEXT, 
	insdc_sample_accession TEXT, 
	"HDBR_accession" TEXT, 
	PRIMARY KEY ("describedBy", schema_version, biomaterial_id, biomaterial_name, biomaterial_description, ncbi_taxon_id, genotype, supplementary_files, biosamples_accession, insdc_sample_accession, "HDBR_accession")
);

CREATE TABLE "CellCycleOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "CellLine" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(11) NOT NULL, 
	provenance TEXT, 
	biomaterial_core TEXT NOT NULL, 
	supplier TEXT, 
	catalog_number TEXT, 
	lot_number TEXT, 
	catalog_url TEXT, 
	cell_cycle TEXT, 
	type VARCHAR(19) NOT NULL, 
	model_organ TEXT NOT NULL, 
	cell_morphology TEXT, 
	growth_conditions TEXT, 
	confluency FLOAT, 
	cell_type TEXT, 
	karyotype TEXT, 
	tissue TEXT, 
	date_established TEXT, 
	disease TEXT, 
	genus_species TEXT, 
	publication TEXT, 
	timecourse TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, biomaterial_core, supplier, catalog_number, lot_number, catalog_url, cell_cycle, type, model_organ, cell_morphology, growth_conditions, confluency, cell_type, karyotype, tissue, date_established, disease, genus_species, publication, timecourse)
);

CREATE TABLE "CellMorphology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	cell_morphology TEXT, 
	cell_size TEXT, 
	cell_size_unit TEXT, 
	percent_cell_viability FLOAT, 
	cell_viability_method TEXT, 
	cell_viability_result VARCHAR(4), 
	percent_necrosis FLOAT, 
	PRIMARY KEY ("describedBy", schema_version, cell_morphology, cell_size, cell_size_unit, percent_cell_viability, cell_viability_method, cell_viability_result, percent_necrosis)
);

CREATE TABLE "CellSuspension" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(11) NOT NULL, 
	provenance TEXT, 
	biomaterial_core TEXT NOT NULL, 
	cell_morphology TEXT, 
	growth_conditions TEXT, 
	genus_species TEXT, 
	selected_cell_types TEXT, 
	estimated_cell_count INTEGER, 
	plate_based_sequencing TEXT, 
	timecourse TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, biomaterial_core, cell_morphology, growth_conditions, genus_species, selected_cell_types, estimated_cell_count, plate_based_sequencing, timecourse)
);

CREATE TABLE "CellTypeOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "CellularComponentOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "Channel" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	channel_id TEXT NOT NULL, 
	excitation_wavelength FLOAT NOT NULL, 
	filter_range TEXT NOT NULL, 
	multiplexed VARCHAR(3) NOT NULL, 
	target_fluorophore TEXT, 
	exposure_time FLOAT NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, channel_id, excitation_wavelength, filter_range, multiplexed, target_fluorophore, exposure_time)
);

CREATE TABLE "CollectionProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	method TEXT NOT NULL, 
	reagents TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, method, reagents)
);

CREATE TABLE "Contact" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	email TEXT, 
	phone TEXT, 
	institution TEXT NOT NULL, 
	laboratory TEXT, 
	address TEXT, 
	country TEXT, 
	corresponding_contributor BOOLEAN, 
	project_role TEXT, 
	orcid_id TEXT, 
	PRIMARY KEY ("describedBy", schema_version, email, phone, institution, laboratory, address, country, corresponding_contributor, project_role, orcid_id)
);

CREATE TABLE "ContributorRoleOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "Death" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	cause_of_death TEXT NOT NULL, 
	cold_perfused BOOLEAN, 
	days_on_ventilator FLOAT, 
	hardy_scale INTEGER, 
	time_of_death TEXT, 
	organ_donation_death_type VARCHAR(38), 
	normothermic_regional_perfusion VARCHAR(7), 
	PRIMARY KEY ("describedBy", schema_version, cause_of_death, cold_perfused, days_on_ventilator, hardy_scale, time_of_death, organ_donation_death_type, normothermic_regional_perfusion)
);

CREATE TABLE "DevelopmentStageOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "DifferentiationProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	method TEXT NOT NULL, 
	media TEXT, 
	small_molecules TEXT, 
	target_cell_yield FLOAT, 
	reagents TEXT, 
	target_pathway TEXT, 
	validation_method TEXT, 
	validation_result TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, method, media, small_molecules, target_cell_yield, reagents, target_pathway, validation_method, validation_result)
);

CREATE TABLE "DiseaseOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "DissociationProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	method TEXT NOT NULL, 
	reagents TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, method, reagents)
);

CREATE TABLE "DonorOrganism" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(11) NOT NULL, 
	provenance TEXT, 
	biomaterial_core TEXT NOT NULL, 
	human_specific TEXT, 
	mouse_specific TEXT, 
	genus_species TEXT, 
	sex VARCHAR(7) NOT NULL, 
	is_living VARCHAR(14) NOT NULL, 
	organism_age TEXT, 
	organism_age_unit TEXT, 
	development_stage TEXT NOT NULL, 
	diseases TEXT, 
	death TEXT, 
	familial_relationships TEXT, 
	medical_history TEXT, 
	gestational_age TEXT, 
	gestational_age_unit TEXT, 
	height TEXT, 
	height_unit TEXT, 
	weight TEXT, 
	weight_unit TEXT, 
	timecourse TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, biomaterial_core, human_specific, mouse_specific, genus_species, sex, is_living, organism_age, organism_age_unit, development_stage, diseases, death, familial_relationships, medical_history, gestational_age, gestational_age_unit, height, height_unit, weight, weight_unit, timecourse)
);

CREATE TABLE "EnrichmentOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "EnrichmentProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	method TEXT NOT NULL, 
	markers TEXT, 
	minimum_size FLOAT, 
	maximum_size FLOAT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, method, markers, minimum_size, maximum_size)
);

CREATE TABLE "Entity" (
	entity_id TEXT NOT NULL, 
	entity_type VARCHAR(7) NOT NULL, 
	PRIMARY KEY (entity_id, entity_type)
);

CREATE TABLE "EthnicityOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "FamilialRelationship" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	parent TEXT, 
	child TEXT, 
	sibling TEXT, 
	PRIMARY KEY ("describedBy", schema_version, parent, child, sibling)
);

CREATE TABLE "FileContentOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "FileCore" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	file_name TEXT NOT NULL, 
	format TEXT NOT NULL, 
	content_description TEXT, 
	checksum TEXT, 
	file_source VARCHAR(20), 
	PRIMARY KEY ("describedBy", schema_version, file_name, format, content_description, checksum, file_source)
);

CREATE TABLE "FileDescriptor" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(15) NOT NULL, 
	file_name TEXT NOT NULL, 
	file_id TEXT NOT NULL, 
	file_version TEXT NOT NULL, 
	content_type TEXT NOT NULL, 
	size INTEGER NOT NULL, 
	sha256 TEXT NOT NULL, 
	crc32c TEXT NOT NULL, 
	sha1 TEXT, 
	s3_etag TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, file_name, file_id, file_version, content_type, size, sha256, crc32c, sha1, s3_etag)
);

CREATE TABLE "FileFormatOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "Funder" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	grant_title TEXT, 
	grant_id TEXT NOT NULL, 
	organization TEXT NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, grant_title, grant_id, organization)
);

CREATE TABLE "GrowthConditions" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	passage_number INTEGER, 
	growth_medium TEXT, 
	culture_environment TEXT, 
	mycoplasma_testing_method VARCHAR(22), 
	mycoplasma_testing_results VARCHAR(4), 
	drug_treatment TEXT, 
	feeder_layer_type VARCHAR(58), 
	PRIMARY KEY ("describedBy", schema_version, passage_number, growth_medium, culture_environment, mycoplasma_testing_method, mycoplasma_testing_results, drug_treatment, feeder_layer_type)
);

CREATE TABLE "HumanSpecific" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	body_mass_index FLOAT, 
	ethnicity TEXT, 
	PRIMARY KEY ("describedBy", schema_version, body_mass_index, ethnicity)
);

CREATE TABLE "ImagedSpecimen" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(11) NOT NULL, 
	provenance TEXT, 
	biomaterial_core TEXT NOT NULL, 
	overview_images TEXT, 
	slice_thickness FLOAT NOT NULL, 
	internal_anatomical_structures TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, biomaterial_core, overview_images, slice_thickness, internal_anatomical_structures)
);

CREATE TABLE "ImageFile" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(4) NOT NULL, 
	provenance TEXT, 
	file_core TEXT NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, file_core)
);

CREATE TABLE "ImagingPreparationProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	fresh_slicing_method TEXT, 
	imaged_slice_thickness FLOAT, 
	final_slicing_method TEXT, 
	post_resection_interval FLOAT, 
	post_resection_interval_unit TEXT, 
	pre_final_slice_preservation_method TEXT, 
	post_final_slicing_interval FLOAT, 
	post_final_slicing_interval_unit TEXT, 
	fiducial_marker TEXT, 
	expansion_factor FLOAT, 
	permeabilisation_time FLOAT, 
	permeabilisation_time_unit TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, fresh_slicing_method, imaged_slice_thickness, final_slicing_method, post_resection_interval, post_resection_interval_unit, pre_final_slice_preservation_method, post_final_slicing_interval, post_final_slicing_interval_unit, fiducial_marker, expansion_factor, permeabilisation_time, permeabilisation_time_unit)
);

CREATE TABLE "ImagingProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	microscope_setup_description TEXT, 
	microscopy_technique TEXT NOT NULL, 
	magnification TEXT NOT NULL, 
	numerical_aperture FLOAT, 
	immersion_medium_type TEXT, 
	immersion_medium_refractive_index FLOAT, 
	pixel_size FLOAT, 
	number_of_tiles INTEGER, 
	tile_size_y FLOAT, 
	tile_size_x FLOAT, 
	z_stack_step_size FLOAT, 
	number_of_z_steps INTEGER, 
	overlapping_tiles VARCHAR(3), 
	channel TEXT, 
	probe TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, microscope_setup_description, microscopy_technique, magnification, numerical_aperture, immersion_medium_type, immersion_medium_refractive_index, pixel_size, number_of_tiles, tile_size_y, tile_size_x, z_stack_step_size, number_of_z_steps, overlapping_tiles, channel, probe)
);

CREATE TABLE "Input" (
	input_type TEXT NOT NULL, 
	input_id TEXT NOT NULL, 
	PRIMARY KEY (input_type, input_id)
);

CREATE TABLE "InsdcExperiment" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	insdc_experiment_accession TEXT NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, insdc_experiment_accession)
);

CREATE TABLE "InstrumentOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "IpscInductionProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	method VARCHAR(19) NOT NULL, 
	reprogramming_factors TEXT, 
	ipsc_induction_kit TEXT, 
	pluripotency_test TEXT, 
	percent_pluripotency FLOAT, 
	pluripotency_vector_removed VARCHAR(7), 
	reagents TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, method, reprogramming_factors, ipsc_induction_kit, pluripotency_test, percent_pluripotency, pluripotency_vector_removed, reagents)
);

CREATE TABLE "LengthUnitOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "LibraryAmplificationOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "LibraryConstructionOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "LibraryPreparationProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	cell_barcode TEXT, 
	spatial_barcode TEXT, 
	input_nucleic_acid_molecule TEXT NOT NULL, 
	nucleic_acid_source VARCHAR(14) NOT NULL, 
	library_construction_method TEXT NOT NULL, 
	library_construction_kit TEXT, 
	nucleic_acid_conversion_kit TEXT, 
	end_bias VARCHAR(16) NOT NULL, 
	primer VARCHAR(7), 
	strand VARCHAR(12) NOT NULL, 
	spike_in_kit TEXT, 
	spike_in_dilution INTEGER, 
	umi_barcode TEXT, 
	library_preamplification_method TEXT, 
	cdna_library_amplification_method TEXT, 
	nominal_length INTEGER, 
	nominal_sdev INTEGER, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, cell_barcode, spatial_barcode, input_nucleic_acid_molecule, nucleic_acid_source, library_construction_method, library_construction_kit, nucleic_acid_conversion_kit, end_bias, primer, strand, spike_in_kit, spike_in_dilution, umi_barcode, library_preamplification_method, cdna_library_amplification_method, nominal_length, nominal_sdev)
);

CREATE TABLE "License" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	identifier TEXT, 
	full_name TEXT, 
	url TEXT, 
	PRIMARY KEY ("describedBy", schema_version, identifier, full_name, url)
);

CREATE TABLE "Links" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(5) NOT NULL, 
	links TEXT NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, links)
);

CREATE TABLE "MassUnitOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "Matrix" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	data_normalization_methods VARCHAR(66), 
	derivation_process VARCHAR(22), 
	PRIMARY KEY ("describedBy", schema_version, data_normalization_methods, derivation_process)
);

CREATE TABLE "MedicalHistory" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	alcohol_history TEXT, 
	medication TEXT, 
	smoking_history TEXT, 
	nutritional_state VARCHAR(20), 
	test_results TEXT, 
	treatment TEXT, 
	PRIMARY KEY ("describedBy", schema_version, alcohol_history, medication, smoking_history, nutritional_state, test_results, treatment)
);

CREATE TABLE "MicroscopyOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "MouseSpecific" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	strain TEXT, 
	PRIMARY KEY ("describedBy", schema_version, strain)
);

CREATE TABLE "Organoid" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(11) NOT NULL, 
	provenance TEXT, 
	biomaterial_core TEXT NOT NULL, 
	genus_species TEXT, 
	model_organ TEXT NOT NULL, 
	model_organ_part TEXT, 
	age FLOAT, 
	age_unit TEXT, 
	size FLOAT, 
	size_unit TEXT, 
	morphology TEXT, 
	embedded_in_matrigel BOOLEAN, 
	growth_environment TEXT, 
	input_aggregate_cell_count FLOAT, 
	stored_oxygen_levels FLOAT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, biomaterial_core, genus_species, model_organ, model_organ_part, age, age_unit, size, size_unit, morphology, embedded_in_matrigel, growth_environment, input_aggregate_cell_count, stored_oxygen_levels)
);

CREATE TABLE "OrganOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "OrganPartOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "Output" (
	output_type TEXT NOT NULL, 
	output_id TEXT NOT NULL, 
	PRIMARY KEY (output_type, output_id)
);

CREATE TABLE "Parameter" (
	checksum TEXT, 
	parameter_name TEXT NOT NULL, 
	parameter_value TEXT NOT NULL, 
	PRIMARY KEY (checksum, parameter_name, parameter_value)
);

CREATE TABLE "PlateBasedSequencing" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	plate_label TEXT NOT NULL, 
	well_label TEXT, 
	well_quality VARCHAR(20), 
	PRIMARY KEY ("describedBy", schema_version, plate_label, well_label, well_quality)
);

CREATE TABLE "PreservationStorage" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	storage_method VARCHAR(25), 
	storage_time FLOAT, 
	storage_time_unit TEXT, 
	preservation_method VARCHAR(49), 
	PRIMARY KEY ("describedBy", schema_version, storage_method, storage_time, storage_time_unit, preservation_method)
);

CREATE TABLE "Probe" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	probe_label TEXT NOT NULL, 
	probe_sequence TEXT, 
	target_name TEXT, 
	target_codebook_label TEXT, 
	target_label TEXT NOT NULL, 
	subcellular_structure TEXT, 
	probe_reagents TEXT, 
	assay_type TEXT NOT NULL, 
	fluorophore TEXT, 
	channel_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, probe_label, probe_sequence, target_name, target_codebook_label, target_label, subcellular_structure, probe_reagents, assay_type, fluorophore, channel_label)
);

CREATE TABLE "Process" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(7) NOT NULL, 
	provenance TEXT, 
	process_core TEXT NOT NULL, 
	start_time TEXT, 
	end_time TEXT, 
	length_of_time TEXT, 
	length_of_time_unit TEXT, 
	type TEXT, 
	deviation_from_protocol TEXT, 
	insdc_experiment TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, process_core, start_time, end_time, length_of_time, length_of_time_unit, type, deviation_from_protocol, insdc_experiment)
);

CREATE TABLE "ProcessCore" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	process_id TEXT NOT NULL, 
	process_name TEXT, 
	process_description TEXT, 
	location TEXT, 
	operators TEXT, 
	PRIMARY KEY ("describedBy", schema_version, process_id, process_name, process_description, location, operators)
);

CREATE TABLE "ProcessLink" (
	process_type TEXT NOT NULL, 
	process_id TEXT NOT NULL, 
	inputs TEXT NOT NULL, 
	outputs TEXT NOT NULL, 
	protocols TEXT NOT NULL, 
	link_type VARCHAR(12) NOT NULL, 
	PRIMARY KEY (process_type, process_id, inputs, outputs, protocols, link_type)
);

CREATE TABLE "ProcessTypeOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "Project" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(7) NOT NULL, 
	provenance TEXT, 
	project_core TEXT NOT NULL, 
	contributors TEXT, 
	supplementary_links TEXT, 
	publications TEXT, 
	insdc_project_accessions TEXT, 
	ega_accessions TEXT, 
	dbgap_accessions TEXT, 
	geo_series_accessions TEXT, 
	array_express_accessions TEXT, 
	insdc_study_accessions TEXT, 
	biostudies_accessions TEXT, 
	funders TEXT NOT NULL, 
	estimated_cell_count INTEGER, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, project_core, contributors, supplementary_links, publications, insdc_project_accessions, ega_accessions, dbgap_accessions, geo_series_accessions, array_express_accessions, insdc_study_accessions, biostudies_accessions, funders, estimated_cell_count)
);

CREATE TABLE "ProjectCore" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	project_short_name TEXT NOT NULL, 
	project_title TEXT NOT NULL, 
	project_description TEXT NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, project_short_name, project_title, project_description)
);

CREATE TABLE "Protocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	type TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, type)
);

CREATE TABLE "ProtocolCore" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	protocol_id TEXT NOT NULL, 
	protocol_name TEXT, 
	protocol_description TEXT, 
	publication_doi TEXT, 
	protocols_io_doi TEXT, 
	document TEXT, 
	PRIMARY KEY ("describedBy", schema_version, protocol_id, protocol_name, protocol_description, publication_doi, protocols_io_doi, document)
);

CREATE TABLE "ProtocolReference" (
	protocol_type VARCHAR(29) NOT NULL, 
	protocol_id TEXT NOT NULL, 
	PRIMARY KEY (protocol_type, protocol_id)
);

CREATE TABLE "ProtocolTypeOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "Provenance" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	schema_major_version INTEGER, 
	schema_minor_version INTEGER, 
	submission_date TEXT NOT NULL, 
	submitter_id TEXT, 
	update_date TEXT, 
	updater_id TEXT, 
	document_id TEXT NOT NULL, 
	accession TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_major_version, schema_minor_version, submission_date, submitter_id, update_date, updater_id, document_id, accession)
);

CREATE TABLE "Publication" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	authors TEXT NOT NULL, 
	title TEXT NOT NULL, 
	doi TEXT, 
	pmid INTEGER, 
	url TEXT, 
	official_hca_publication BOOLEAN NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, authors, title, doi, pmid, url, official_hca_publication)
);

CREATE TABLE "PurchasedReagents" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	retail_name TEXT, 
	catalog_number TEXT, 
	manufacturer TEXT, 
	lot_number TEXT, 
	expiry_date TEXT, 
	kit_titer TEXT, 
	PRIMARY KEY ("describedBy", schema_version, retail_name, catalog_number, manufacturer, lot_number, expiry_date, kit_titer)
);

CREATE TABLE "ReferenceFile" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(4) NOT NULL, 
	provenance TEXT, 
	file_core TEXT NOT NULL, 
	ncbi_taxon_id INTEGER NOT NULL, 
	genus_species TEXT NOT NULL, 
	reference_type VARCHAR(22) NOT NULL, 
	assembly_type VARCHAR(17) NOT NULL, 
	reference_version TEXT NOT NULL, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, file_core, ncbi_taxon_id, genus_species, reference_type, assembly_type, reference_version)
);

CREATE TABLE "S10x" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	fastq_method TEXT, 
	fastq_method_version TEXT, 
	pooled_channels FLOAT, 
	drop_uniformity BOOLEAN, 
	PRIMARY KEY ("describedBy", schema_version, fastq_method, fastq_method_version, pooled_channels, drop_uniformity)
);

CREATE TABLE "SequenceFile" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(4) NOT NULL, 
	provenance TEXT, 
	file_core TEXT NOT NULL, 
	read_index VARCHAR(23) NOT NULL, 
	lane_index INTEGER, 
	read_length INTEGER, 
	insdc_run_accessions TEXT, 
	library_prep_id TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, file_core, read_index, lane_index, read_length, insdc_run_accessions, library_prep_id)
);

CREATE TABLE "SequencingOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "SequencingProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	instrument_manufacturer_model TEXT NOT NULL, 
	local_machine_name TEXT, 
	paired_end BOOLEAN NOT NULL, 
	method TEXT NOT NULL, 
	s10x TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, instrument_manufacturer_model, local_machine_name, paired_end, method, s10x)
);

CREATE TABLE "SpeciesOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "SpecimenFromOrganism" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(11) NOT NULL, 
	provenance TEXT, 
	biomaterial_core TEXT NOT NULL, 
	genus_species TEXT, 
	organ TEXT NOT NULL, 
	organ_parts TEXT, 
	diseases TEXT, 
	state_of_specimen TEXT, 
	preservation_storage TEXT, 
	collection_time TEXT, 
	purchased_specimen TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, biomaterial_core, genus_species, organ, organ_parts, diseases, state_of_specimen, preservation_storage, collection_time, purchased_specimen)
);

CREATE TABLE "StateOfSpecimen" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	autolysis_score VARCHAR(8), 
	gross_description TEXT, 
	gross_images TEXT, 
	ischemic_temperature VARCHAR(4), 
	ischemic_time INTEGER, 
	microscopic_description TEXT, 
	microscopic_images TEXT, 
	postmortem_interval INTEGER, 
	PRIMARY KEY ("describedBy", schema_version, autolysis_score, gross_description, gross_images, ischemic_temperature, ischemic_time, microscopic_description, microscopic_images, postmortem_interval)
);

CREATE TABLE "StrainOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "SupplementaryFile" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(4) NOT NULL, 
	provenance TEXT, 
	file_core TEXT NOT NULL, 
	file_description TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, file_core, file_description)
);

CREATE TABLE "SupplementaryFileEntity" (
	file_id TEXT NOT NULL, 
	file_type VARCHAR(18) NOT NULL, 
	PRIMARY KEY (file_id, file_type)
);

CREATE TABLE "SupplementaryFileLink" (
	entity TEXT NOT NULL, 
	files TEXT NOT NULL, 
	link_type VARCHAR(23) NOT NULL, 
	PRIMARY KEY (entity, files, link_type)
);

CREATE TABLE "TargetPathwayOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "Task" (
	disk_size TEXT NOT NULL, 
	task_name TEXT NOT NULL, 
	zone TEXT NOT NULL, 
	log_err TEXT, 
	start_time TEXT NOT NULL, 
	cpus INTEGER NOT NULL, 
	log_out TEXT, 
	stop_time TEXT NOT NULL, 
	memory TEXT NOT NULL, 
	docker_image TEXT NOT NULL, 
	PRIMARY KEY (disk_size, task_name, zone, log_err, start_time, cpus, log_out, stop_time, memory, docker_image)
);

CREATE TABLE "Timecourse" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	value TEXT NOT NULL, 
	unit TEXT NOT NULL, 
	relevance TEXT, 
	PRIMARY KEY ("describedBy", schema_version, value, unit, relevance)
);

CREATE TABLE "TimeUnitOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "TreatmentMethodOntology" (
	"describedBy" TEXT, 
	schema_version TEXT, 
	text TEXT NOT NULL, 
	ontology VARCHAR, 
	ontology_label TEXT, 
	PRIMARY KEY ("describedBy", schema_version, text, ontology, ontology_label)
);

CREATE TABLE "TreatmentProtocol" (
	"describedBy" TEXT NOT NULL, 
	schema_version TEXT, 
	schema_type VARCHAR(8) NOT NULL, 
	provenance TEXT, 
	protocol_core TEXT NOT NULL, 
	method TEXT NOT NULL, 
	media TEXT, 
	reagents TEXT, 
	target_pathway TEXT, 
	PRIMARY KEY ("describedBy", schema_version, schema_type, provenance, protocol_core, method, media, reagents, target_pathway)
);
