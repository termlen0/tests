#!/usr/bin/env python
import textfsm
import os.path
import pytest

def test_textfsm_12():
    # Assert that the files exist
    assert os.path.isfile('cisco_nxos_show_ip_interface_brief.raw')
    assert os.path.isfile('cisco_nxos_show_ip_interface_brief.template')
    # Load the input file to a variable
    input_file = open("cisco_nxos_show_ip_interface_brief.raw")
    raw_text_data = input_file.read()
    input_file.close()

    # Run the text through the FSM.
    template = open("cisco_nxos_show_ip_interface_brief.template")
    re_table = textfsm.TextFSM(template)
    fsm_results = re_table.ParseText(raw_text_data)


    print(fsm_results[0])
    #print(re_table.header)

    # Assert that the values captured by textfsm are valid
    intf = fsm_results[0]
    assert intf[0] == 'Vlan10'
    assert intf[1] == '10.20.10.1'
    assert intf[2] == 'down'
    assert intf[3] == 'down'
    assert intf[4] == 'down'
    # Assert that the header returned by textfsm is accurate
    header = re_table.header
    assert header[0] == 'INTERFACE'
    assert header[1] == 'IP'
    assert header[2] == 'PROTOCOL'
    assert header[3] == 'STATUS'
    assert header[4] == 'ADMIN'
