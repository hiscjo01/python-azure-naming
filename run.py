#!/usr/bin/python

import requests
from requests.exceptions import HTTPError

import yaml
import os.path

from mdutils import MdUtils

def importEntity(url, entity_yaml):
    # Fetch information from M$oft and parse
    contents = webScrape(url)
    entities = parseMarkdown(contents)
    
    # Open local data and merge
    if os.path.isfile(entity_yaml): 
        local_entities = yaml.load(
                            open(entity_yaml),
                            Loader=yaml.FullLoader)

        combined_entities = {**entities,**local_entities}
        entities = combined_entities
    
    # Write output data
    yaml.dump(entities, 
              open(entity_yaml, 'w'),
              indent=4, 
              sort_keys=False,
              default_flow_style=False)

    return entities

def parseMarkdown(content):

    entities = dict()

    # Split markdown into sections based on header tag
    sections = content.decode('utf8').strip('\n').split('## ')
    
    for section in sections:
        
        lines = section.split('\n')
        
        # Split section into lines based on crlf
        for line in lines:
            
            if line.startswith('Microsoft.'): 
                
                category = line[10:]
            
            elif line.startswith('> |'):
                
                # This is a row that contains a naming rule
                fields = line.split('|')
                
                if ((fields[1].strip(' ') != 'Entity') and 
                    (fields[1].strip(' ') != '---')):
                    
                    #Extract data
                    path = fields[1].strip(' ').replace(" ", "")
                    entity = path.split("/")[-1]
                    scope = fields[2].strip(' ')
                    length = fields[3].strip(' ')
                    maxlength = length.split("-")[-1]
                    rules = fields[4].strip(' ').lower()

                    # Normalize data
                    if (("63 characters" in maxlength) or
                        (maxlength == '')): 
                        
                        maxlength = "63"
                    elif("98" in maxlength): 
                        maxlength = "98"
                    elif("64" in maxlength):
                        maxlength = "64"
                    elif("bit integer" in maxlength):
                        maxlength = "64"
                    elif("resource name" in maxlength):
                        maxlength = "255"

                    if (("hyphen" in rules) or
                        ("%" in rules) or
                        ("[]" in rules) or
                        ("&" in rules) or
                        ("any url" in rules) or
                        ("all characters" in rules)): 
                        
                        rules = "a-9"
                    
                    elif (("letters and numbers" in rules) or
                        ("letters or numbers" in rules) or
                        ("alphanumerics" in rules)): 
                        
                        rules = "a9"

                    elif("default" in rules):
                        rules = "default"

                    elif("numbers and periods" in rules):
                        rules = "0.9"

                    # Add to dictionary
                    if path not in entities.keys(): entities[path] = list()
                    
                    entities[path].append({
                            'category' : category,
                            'entity' : entity,
                            'scope' : scope,
                            'maxlength': maxlength,
                            'rule': rules,
                            'convention': '',
                            'example': ''
                        })
                    
    return entities
            
def webScrape(url):
    # Go fetch the markdown from the web
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.8
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.8
    else:
        #  Request was successful
        return response.content

def importCustom(custom_yaml):
    if os.path.isfile(custom_yaml): 
        
        custom_entities = yaml.load(
                            open(custom_yaml),
                            Loader=yaml.FullLoader)

        for e in custom_entities:
            

            maxlength = custom_entities[e][0]['maxlength']
            rule = custom_entities[e][0]['rule']
            allowed_values = custom_entities[e][0]['allowed_values']
            # Loop through the list of allowed values and check
            for v in allowed_values:
                
                for key,value in v.items():
                # Couple of checks to do some validation of the data
                    
                    # Blow up if user entered value greater than the allowed length.
                    if len(key) > int(maxlength): 
                        raise ValueError("Length of "+key+" exceeds maximum value of "
                                        +maxlength+" set for this entity.")
                
                    # And if they say lowercase and alphanumeric and it isnt
                    if ((rule == 'az') 
                        and (
                            not key.islower() 
                            or not key.isalnum()
                        )):
                        raise ValueError("You have specified convention is "+
                                        rule+" but your allowed value contains "+
                                        key)
                    
                    # If they just specify lower
                    if (rule == 'a-z') and not key.islower():
                        raise ValueError("You have specified convention is "+
                                        rule+" but your allowed value contains "+
                                        key)
                    

        return custom_entities

def exportMarkdown(title,custom,entities):
    mdf = MdUtils(file_name='README',title=title)
    
    # Create the Overview Section
    mdf.new_header(level=1, title='Overview')
    mdf.new_paragraph(
        "This is the overview section.  Blah blah blah"
        "more blah blah"
    )

    # Create the Custom Entity Section
    mdf.new_header(level=1, title='RBA Entities')
    mdf.new_paragraph(
        "This can describe the purpose for the RBA entities. It is meant as"
        "a placeholder for whatever we want to say about them."
    )

    # Role through the custom dictionary
    for entity in sorted(custom):
        mdf.new_header(level=2, title='rba.'+entity)
        
        entity_tbl = [
            '<sub>Full Text</sub>',
            '<sub>Scope</sub>',
            '<sub>Rule</sub>',
            '<sub>Value</sub>'
        ]
        
        entity_lst = custom[entity][0]['allowed_values']
        entity_count = len(entity_lst)+1
        
        scope = custom[entity][0]['scope']
        rule = custom[entity][0]['rule']+'['+custom[entity][0]['maxlength']+']'
        
        for item in entity_lst:
            for key,value in item.items():
                long_name = value
                variable = key
                entity_tbl.extend([
                    '<sub>' + long_name + '</sub>',
                    '<sub>' + scope + '</sub>',
                    '<sub>' + rule + '</sub>',
                    '<sub>' + variable + '</sub>'
                ])

        mdf.new_table(columns=4,rows=entity_count,text=entity_tbl,text_align='center')

    # Create the Azure Entity Section
    mdf.new_header(level=1, title='Azure Entities')
    mdf.new_paragraph(
        "This can describe the purpose for the custom entities. It is meant as"
        "a placeholder for whatever we want to say about them."
    )

    category_lst = {}
    for entity in entities:
        for e in entities[entity]:
            category = e['category']
            
            if category not in category_lst.keys(): category_lst[category] = []
            
            category_lst[category].append(entity)
    
    for category in sorted(category_lst):
        mdf.new_header(level=2, title='azure.'+category)

        entity_count = len(category_lst[category]) + 1
        entity_tbl = [
            '<sub>Entity</sub>',
            '<sub>Scope</sub>',
            '<sub>Rule</sub>',
            '<sub>Convention</sub>',
            '<sub>Example</sub>'
        ]

        for entity in sorted(category_lst[category]):

            for e in entities[entity]:
                category_name = e['category']
                if category_name == category:
                    entity_name = e['entity']
                    scope = e['scope']
                    rule = e['rule']+'['+e['maxlength']+']'
                    convention = e['convention']
                    example = e['example']
            
                    entity_tbl.extend([
                        '<sub>' + entity_name + '</sub>',
                        '<sub>' + scope + '</sub>',
                        '<sub>' + rule + '</sub>',
                        '<sub>' + convention + '</sub>',
                        '<sub>' + example + '</sub>'
                    ])
            
        mdf.new_table(columns=5,rows=entity_count,text=entity_tbl,text_align='center')


    # Write the markdown file
    mdf.create_md_file()  

def createLinks(custom,entities):
    with open('README.md', 'r') as file:
       filedata = file.read()
    
    # Handle the gitlab table thing
    filedata = filedata.replace(':---:','------')

    # Go through the custom entities and create links
    for entity in custom:
        maxlength = custom[entity][0]['maxlength']
        filedata = filedata.replace('<rba.'+entity,'<[rba.'+entity+'['+maxlength+']](README.md#rba'+entity+')')

    with open('README.md', 'w') as file:
        file.write(filedata) 

def main():
    url = ('https://raw.githubusercontent.com/MicrosoftDocs/'+
            'azure-docs/master/articles/azure-resource-manager/'+
            'management/resource-name-rules.md')
    entity_yaml = "entity.yaml"
    custom_yaml = 'custom.yaml'
    
    entities = importEntity(url,entity_yaml)
    custom = importCustom(custom_yaml)

    exportMarkdown('RBA Naming Conventions for Azure',custom,entities)
    createLinks(custom,entities)

if __name__ == '__main__':
    main()