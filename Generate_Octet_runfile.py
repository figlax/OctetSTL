from OctetSTL import *

#Use this file to generate octet stl files using OctetSTL
def main():

    sw = 0.6
    cf = 5.0
    x = 10
    y = 10
    z = 10
    rd = 0.05  # target relative density
    pitch = 6.04 # only enter pitch if not generating from specified rd
    # test_cap = cap(strut_width, chamfer_factor, pitch)
    # test_corner = corner(strut_width, chamfer_factor, pitch)
    test_node = node(sw, cf)
    # test_voxel = voxel(strut_width, chamfer_factor, pitch)
    # test_corner_node = corner_node(strut_width, chamfer_factor)


    generated_pitch = pitch_from_relden(rd, cf, sw) # calculate the pitch from a target relative density
    print ("For relative density %s, the calculated pitch is %s" %(str(rd), str(generated_pitch)))

    test_lattice = make_lattice(sw, cf, generated_pitch, x, y, z)

    stl_file_name = generate_file_name(sw, cf, x, y, z, generated_pitch, rd)

    test_lattice.save('generated_stl_files/' + stl_file_name)
    # test_node.save('test_octet_closed_node.stl')
    print ("File saved as %s" %stl_file_name)

    #preview_mesh(test_cap)

if __name__ == "__main__":
    main()