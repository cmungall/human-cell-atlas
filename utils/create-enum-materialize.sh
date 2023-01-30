grep _ontology_options src/human_cell_atlas/schema/module/ontology/*yaml | perl -npe 's@^(.*.yaml):  (\w+_ontology_options)@vskit -vv expand -s $1.yaml -o $1.expanded.yaml $2\n@' | grep vsk
