import os
import pathlib

input_directory = 'quality_base'
output_directory = 'configuration/quality'

# variants are shown as the nozzel in Cura
variants = ['0.2 mm', '0.3 mm', '0.4 mm', '0.5 mm', '0.6 mm', '0.8 mm']
variants_pva = ['PVA 0.4mm', 'PVA 0.5mm', 'PVA 0.6mm', 'PVA 0.8mm']

# Assign material and varaints
material_matrix = {
    'generic_abs_175':  variants,
    'generic_petg_175': variants,
    'generic_pla_175':  variants,
    'generic_pva_175':  variants_pva
}

def main():
    print('Generating profiles for Cura...')

    script_directory = pathlib.Path.cwd()
    output_path = script_directory.parents[0] / output_directory
    base_quality_directory = script_directory / input_directory
    base_quality_files = os.listdir(base_quality_directory)

    print(base_quality_files)

    for base_file_name in base_quality_files: 
        base_file_pathname = base_quality_directory / base_file_name
        with open(base_file_pathname, "rt") as base_file:
            for material in material_matrix:
                print(material)
                for variant in material_matrix[material]:
                    print(variant)
                    # Generate output filename according to material and variant (nozzel)
                    output_filename = base_file_name[:5] + '_' + variant.replace(' ', '') + '_' + material + base_file_name[5:]
                    output_file_pathname = output_path / output_filename
                    print(output_file_pathname)
                    with open(output_file_pathname, "wt") as output_file:
                        # reset read pointer to beginning
                        base_file.seek(0)
                        # replace variables with real value
                        for line in base_file:
                            output_file.write(line.replace('%material%', material).replace('%variant%', variant))

if __name__ == "__main__":
    # execute only if run as a script
    main()