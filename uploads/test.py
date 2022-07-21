#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import socket
import argparse
import subprocess as sp

CMD = '/opt/yugabyte-2.13.0.0/bin/yb-admin -master_addresses 98.8.94.65:7100,98.8.94.66:7100,98.8.94.67:7100 list_all_tablet_servers'

MEMORY_WARRNING_HELP = "Memory Threshold for warring in percentage"
MEMORY_CRITICAL_HELP = "Memory Threshold for critical in percentage"
READ_WARRNING_HELP = "Reads/s Threshold for warning in percentage"
READ_CRITICAL_HELP = "Reads/s Threshold for critical in percentage"
WRITE_WARRNING_HELP = "Writes/s Threshold for warring in percentage"
WRITE_CRITICAL_HELP = "Writes/s Threshold for critical in percentage"
UPTIME_WARRNING_HELP = "Uptime Threshold for warning in percentage"
UPTIME_CRITICAL_HELP = "Uptime Threshold for critical in percentage"
SST_TOTAL_WARRNING_HELP = "ST Total Size Threshold for warning in percentage"
SST_TOTAL_CRITICAL_HELP = "ST Total Size Threshold for critical in percentage"
SST_TOTAL_UNC_WARRNING_HELP = "SST Uncomp Size Threshold for warning in percentage"
SST_TOTAL_UNC_CRITICAL_HELP = "ST Uncomp Size Threshold for critical in percentage"
FILES_WARRNING_HELP = "ST Files Threshold for warning in percentage"
FILES_CRITICAL_HELP = "ST Files Threshold for critical in percentage"

ARGS_MAPPING = {
    'read': 'Reads/s',
    'write': 'Writes/s',
    'uptime': 'Uptime',
    'sst_total': 'SST total size',
    'sst_total_unc': 'SST uncomp size',
    'files': '#files',
}


def validate_args(arguments):
    for arg in arguments:
        name, _type = arg.split("_")
        if _type == "warn" and "{}_critical".format(name) not in arguments:
            print("Error: Warning Threshold Provided for {} but Critical Threshold is missing".format(name))
        if _type == "critical" and "{}_warn".format(name) not in arguments:
            print("Error: Critical Threshold Provided for {} but Warning Threshold is missing".format(name))


def get_options():
    global kwargs
    parser = argparse.ArgumentParser()
    parser.add_argument('-tw', '--threshold_warn', type=int, help=MEMORY_WARRNING_HELP, required=True)
    parser.add_argument('-tc', '--threshold_critical', type=int,help=MEMORY_CRITICAL_HELP, required=True)
    parser.add_argument('-ww', '--write_warn', type=str, help=READ_WARRNING_HELP)
    parser.add_argument('-wc', '--write_critical', type=str,help=READ_CRITICAL_HELP)
    parser.add_argument('-rw', '--read_warn', type=str, help=WRITE_WARRNING_HELP)
    parser.add_argument('-rc', '--read_critical', type=str,help=WRITE_CRITICAL_HELP)
    parser.add_argument('-uw', '--uptime_warn', type=str,help=UPTIME_WARRNING_HELP)
    parser.add_argument('-uc', '--uptime_critical', type=str,help=UPTIME_CRITICAL_HELP)
    parser.add_argument('-stw', '--sst_total_warn', type=str,help=SST_TOTAL_WARRNING_HELP)
    parser.add_argument('-stc', '--sst_total_critical', type=str,help=SST_TOTAL_CRITICAL_HELP)
    parser.add_argument('-stuw', '--sst_total_unc_warn', type=str,help=SST_TOTAL_UNC_WARRNING_HELP)
    parser.add_argument('-stuc', '--sst_total_unc_critical', type=str,help=SST_TOTAL_UNC_CRITICAL_HELP)
    parser.add_argument('-fw', '--files_warn', type=str,help=FILES_WARRNING_HELP)
    parser.add_argument('-fc', '--files_critical', type=str,help=FILES_CRITICAL_HELP)

    args = parser.parse_args()
    kwargs = dict(args._get_kwargs())
    kwargs = {k:v for k,v in kwargs.items() if v is not None}
    validate_args(kwargs)


def cmd_response():
    data = sp.check_output(CMD, shell=True)
    return data


def find_my_ip():
    global ip_address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def find_my_memory():
    global system_memory
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    mem_gib = mem_bytes / 1024.0 ** 3
    system_memory = round(mem_gib, 2)
    return round(mem_gib, 2)


def output_to_dict(data):
    columns = [
        'Tablet Server UUID',
        'RPC Host/Port',
        'Heartbeat delay',
        'Status',
        'Reads/s',
        'Writes/s',
        'Uptime',
        'SST total size',
        'SST uncomp size',
        '#files',
        'Memory',
    ]

    response = []
    for (idx, row) in enumerate(data.split('\n')):
        if idx == 0 or row == '':
            continue

    row = row.replace(' GB', '').split(' ')
    row = [i for i in row if i != '']

    res = {}
    for (idx, col) in enumerate(columns):
        res.update({'{}'.format(col): row[idx]})
        response.append(res)
    return response


def health_check(data):
    host = find_my_ip()
    memory = find_my_memory()
    node = next(i for i in data if host in i['RPC Host/Port'])
    usage = round(float(node['Memory']) * 100 / float(memory), 2)
    if usage == None:
        return ('UNKNOWN', node)
    elif usage >= kwargs['threshold_critical']:
        return ('CRITICAL', node)
    elif usage > kwargs['threshold_warn']:
        return ('WARNING', node)
    else:
        return ('OK', node)


def op5_output(status, node):
    host = find_my_ip()

    memory = find_my_memory()

    output = ''
    if 'read_warn' in kwargs or 'read_critical' in kwargs:
        opt = ' | {}_read={};{};{}'.format(host, node[ARGS_MAPPING.get('read')], kwargs['read_warn'], kwargs['read_critical'])
        output += opt
    if 'write_warn' in kwargs or 'write_critical' in kwargs:
        opt = ' | {}_write={};{};{}'.format(host, node[ARGS_MAPPING.get('write')], kwargs['write_warn'], kwargs['write_critical'])
        output += opt
    if 'uptime_warn' in kwargs or 'uptime_critical' in kwargs:
        
        opt = ' | {}_uptime={};{};{}'.format(host, node[ARGS_MAPPING.get('uptime')], kwargs['uptime_warn'], kwargs['uptime_critical'])
        output += opt
    if 'sst_total_warn' in kwargs or 'sst_total_critical' in kwargs:
        opt = ' | {}_sst_total={};{};{}'.format(host, node[ARGS_MAPPING.get('sst_total')], kwargs['sst_total_warn'], kwargs['sst_total_critical'])
        output += opt
    if 'sst_total_unc_warn' in kwargs or 'sst_total_unc_critical' in kwargs:
        opt = ' | {}_sst_total_unc={};{};{}'.format(host, node[ARGS_MAPPING.get('sst_total_unc')], kwargs['sst_total_unc_warn'], kwargs['sst_total_unc_critical'])
        output += opt
    if 'files_warn' in kwargs or 'files_critical' in kwargs:
        opt = ' | {}_files={};{};{}'.format(host, node[ARGS_MAPPING.get('files')], kwargs['files_warn'], kwargs['files_critical'])
        output += opt

    if status == 'UNKNOWN':
        print('UNKNOWN: Unknown error while checking the usage' + output)
        exit(3)
    if status == 'CRITICAL':
        MSG = 'CRITICAL: The current node is above Critical Threshold | {}_memory={};{};{}'
        print(MSG.format(host, node['Memory'], memory * kwargs['threshold_warn'] / 100, memory * kwargs['threshold_critical'] / 100) + output)
        exit(2)
    elif status == 'WARNING':
        MSG = 'WARNING: The current node is above Warning Threshold | {}_memory={};{};{}'
        print(MSG.format( host, node['Memory'], memory * kwargs['threshold_warn'] / 100, memory * kwargs['threshold_critical'] / 100) + output)
        exit(1)
    else:
        MSG = 'OK: The current node is below the Warning/Critical Threshold | {}_memory={};{};{}'
        print(MSG.format( host, node['Memory'], memory * kwargs['threshold_warn'] / 100, memory * kwargs['threshold_critical'] / 100) + output)
        exit(0)


if __name__ == '__main__':
    get_options()
    # data = cmd_response()
    # dict_response = output_to_dict(data)
    # (status, node) = health_check(dict_response)
    # op5_output(status, node)
