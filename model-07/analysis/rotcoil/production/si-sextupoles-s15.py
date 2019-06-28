#!/usr/bin/env python-sirius
"""."""

import numpy as np
import matplotlib.pyplot as plt


multipole_index = 2


family_1 = [
    'S15-050', 'S15-141', 'S15-177', 'S15-044', 'S15-256', 'S15-251', 'S15-102',
    'S15-107', 'S15-281', 'S15-006', 'S15-232', 'S15-261', 'S15-139', 'S15-272',
    'S15-118', 'S15-165', 'S15-227', 'S15-140', 'S15-043', 'S15-131', 'S15-216',
    'S15-076', 'S15-087', 'S15-008', 'S15-056', 'S15-159', 'S15-167', 'S15-101',
    'S15-146', 'S15-035', 'S15-133', 'S15-195', 'S15-142', 'S15-104', 'S15-103',
    'S15-091', 'S15-197', 'S15-179', 'S15-275', 'S15-242', 'S15-166', 'S15-231',
    'S15-164', 'S15-258', 'S15-121', 'S15-078', 'S15-122', 'S15-180', 'S15-093',
    'S15-176', 'S15-218', 'S15-253', 'S15-092', 'S15-212', 'S15-136', 'S15-070',
    'S15-032', 'S15-276', 'S15-117', 'S15-277', 'S15-148', 'S15-014', 'S15-113',
    'S15-105', 'S15-127', 'S15-124', 'S15-191', 'S15-051', 'S15-004', 'S15-126',
    'S15-174', 'S15-026', 'S15-036', 'S15-278', 'S15-209', 'S15-027', 'S15-134',
    'S15-192', 'S15-059', 'S15-234', 'S15-116', 'S15-143', 'S15-017', 'S15-061',
    'S15-185', 'S15-041', 'S15-263', 'S15-168', 'S15-033', 'S15-267', 'S15-045',
    'S15-171', 'S15-184', 'S15-155', 'S15-248', 'S15-132', 'S15-229', 'S15-213',
    'S15-040', 'S15-183', 'S15-206', 'S15-271', 'S15-110', 'S15-186', 'S15-062',
    'S15-228', 'S15-210', 'S15-109', 'S15-156', 'S15-029', 'S15-181', 'S15-194',
    'S15-079', 'S15-246', 'S15-046', 'S15-219', 'S15-274', 'S15-149', 'S15-187',
    'S15-021', 'S15-053', 'S15-223', 'S15-057', 'S15-138', 'S15-239', 'S15-100',
    'S15-172', 'S15-245', 'S15-018', 'S15-145', 'S15-052', 'S15-072', 'S15-038',
    'S15-170', 'S15-111', 'S15-031', 'S15-058', 'S15-157', 'S15-137', 'S15-220',
    'S15-016', 'S15-130', 'S15-215', 'S15-237', 'S15-244', 'S15-055', 'S15-128',
    'S15-221', 'S15-119', 'S15-193', 'S15-106', 'S15-188', 'S15-190', 'S15-222',
    'S15-207', 'S15-099', 'S15-257', 'S15-238', 'S15-010', 'S15-009', 'S15-123',
    'S15-054', 'S15-034', 'S15-230', 'S15-154', 'S15-199', 'S15-120', 'S15-162',
    'S15-037', 'S15-047', 'S15-030', 'S15-249', 'S15-240', 'S15-060', 'S15-048',
    'S15-189', 'S15-175', 'S15-236', ]


family_2 = [
    'S15-225', 'S15-090', 'S15-198', 'S15-028', 'S15-282', 'S15-214', 'S15-063',
    'S15-068', 'S15-019', 'S15-259', 'S15-286', 'S15-135', 'S15-097', 'S15-208',
    'S15-115', 'S15-268', 'S15-023', 'S15-005', 'S15-015', 'S15-163', 'S15-098',
    'S15-080', 'S15-086', 'S15-217', 'S15-025', 'S15-082', 'S15-204', 'S15-266',
    'S15-049', 'S15-011', 'S15-260', 'S15-182', 'S15-235', 'S15-042', 'S15-196',
    'S15-012', 'S15-270', 'S15-169', 'S15-200', 'S15-085', 'S15-084', 'S15-039',
    'S15-151', 'S15-284', 'S15-233', 'S15-243', 'S15-280', 'S15-283', 'S15-074',
    'S15-178', 'S15-022', 'S15-203', 'S15-073', 'S15-083', 'S15-024', 'S15-264',
    'S15-067', 'S15-094', 'S15-265', 'S15-279', 'S15-144', 'S15-173', 'S15-285',
    'S15-112', 'S15-269', 'S15-161', 'S15-007', 'S15-241', 'S15-224', 'S15-064',
    'S15-205', 'S15-108', 'S15-262', 'S15-075', 'S15-226', 'S15-250', 'S15-152',
    'S15-129', 'S15-255', 'S15-150', 'S15-273', 'S15-089', 'S15-147', 'S15-252',
    'S15-201', 'S15-211', 'S15-020', 'S15-077', 'S15-071', 'S15-158', 'S15-013',
    'S15-160', 'S15-114', 'S15-096', 'S15-095', 'S15-247', 'S15-081', 'S15-153',
    'S15-254', 'S15-088', 'S15-065', 'S15-125', 'S15-202', ]


fams = {
    'SDA0': {
        'current_str': '50',
        'sorting': {
            'SI-01M2:MA-SDA0': 'S15-004',
            'SI-05M1:MA-SDA0': 'S15-007',
            'SI-05M2:MA-SDA0': 'S15-270',
            'SI-09M1:MA-SDA0': 'S15-240',
            'SI-09M2:MA-SDA0': 'S15-283',
            'SI-13M1:MA-SDA0': 'S15-122',
            'SI-13M2:MA-SDA0': 'S15-184',
            'SI-17M1:MA-SDA0': 'S15-273',
            'SI-17M2:MA-SDA0': 'S15-118',
            'SI-01M1:MA-SDA0': 'S15-261',
        },
        'color': 'b'},
    'SFA0': {
        'current_str': '30',
        'sorting': {
            'SI-01M2:MA-SFA0': 'S15-278',
            'SI-05M1:MA-SFA0': 'S15-246',
            'SI-05M2:MA-SFA0': 'S15-276',
            'SI-09M1:MA-SFA0': 'S15-009',
            'SI-09M2:MA-SFA0': 'S15-015',
            'SI-13M1:MA-SFA0': 'S15-279',
            'SI-13M2:MA-SFA0': 'S15-033',
            'SI-17M1:MA-SFA0': 'S15-016',
            'SI-17M2:MA-SFA0': 'S15-010',
            'SI-01M1:MA-SFA0': 'S15-172',
        },
        'color': 'g'},
    'SDB0': {
        'current_str': '50',
        'sorting': {
            'SI-02M1:MA-SDB0': 'S15-159',
            'SI-02M2:MA-SDB0': 'S15-119',
            'SI-04M1:MA-SDB0': 'S15-132',
            'SI-04M2:MA-SDB0': 'S15-101',
            'SI-06M1:MA-SDB0': 'S15-026',
            'SI-06M2:MA-SDB0': 'S15-085',
            'SI-08M1:MA-SDB0': 'S15-259',
            'SI-08M2:MA-SDB0': 'S15-264',
            'SI-10M1:MA-SDB0': 'S15-154',
            'SI-10M2:MA-SDB0': 'S15-131',
            'SI-12M1:MA-SDB0': 'S15-241',
            'SI-12M2:MA-SDB0': 'S15-108',
            'SI-14M1:MA-SDB0': 'S15-086',
            'SI-14M2:MA-SDB0': 'S15-114',
            'SI-16M1:MA-SDB0': 'S15-213',
            'SI-16M2:MA-SDB0': 'S15-106',
            'SI-18M1:MA-SDB0': 'S15-157',
            'SI-18M2:MA-SDB0': 'S15-023',
            'SI-20M1:MA-SDB0': 'S15-045',
            'SI-20M2:MA-SDB0': 'S15-239',
        },
        'color': 'r'},
    'SFB0': {
        'current_str': '50',
        'sorting': {
            'SI-02M1:MA-SFB0': 'S15-076',
            'SI-02M2:MA-SFB0': 'S15-133',
            'SI-04M1:MA-SFB0': 'S15-152',
            'SI-04M2:MA-SFB0': 'S15-082',
            'SI-06M1:MA-SFB0': 'S15-074',
            'SI-06M2:MA-SFB0': 'S15-163',
            'SI-08M1:MA-SFB0': 'S15-103',
            'SI-08M2:MA-SFB0': 'S15-075',
            'SI-10M1:MA-SFB0': 'S15-072',
            'SI-10M2:MA-SFB0': 'S15-208',
            'SI-12M1:MA-SFB0': 'S15-039',
            'SI-12M2:MA-SFB0': 'S15-048',
            'SI-14M1:MA-SFB0': 'S15-070',
            'SI-14M2:MA-SFB0': 'S15-053',
            'SI-16M1:MA-SFB0': 'S15-038',
            'SI-16M2:MA-SFB0': 'S15-151',
            'SI-18M1:MA-SFB0': 'S15-077',
            'SI-18M2:MA-SFB0': 'S15-013',
            'SI-20M1:MA-SFB0': 'S15-056',
            'SI-20M2:MA-SFB0': 'S15-073',
        },
        'color': 'k'},
    'SDP0': {
        'current_str': '50',
        'sorting': {
            'SI-03M1:MA-SDP0': 'S15-041',
            'SI-03M2:MA-SDP0': 'S15-110',
            'SI-07M1:MA-SDP0': 'S15-113',
            'SI-07M2:MA-SDP0': 'S15-269',
            'SI-11M1:MA-SDP0': 'S15-230',
            'SI-11M2:MA-SDP0': 'S15-147',
            'SI-15M1:MA-SDP0': 'S15-143',
            'SI-15M2:MA-SDP0': 'S15-193',
            'SI-19M1:MA-SDP0': 'S15-232',
            'SI-19M2:MA-SDP0': 'S15-187',
        },
        'color': 'y'},
    'SFP0': {
        'current_str': '50',
        'sorting': {
            'SI-03M1:MA-SFP0': 'S15-249',
            'SI-03M2:MA-SFP0': 'S15-221',
            'SI-07M1:MA-SFP0': 'S15-238',
            'SI-07M2:MA-SFP0': 'S15-044',
            'SI-11M1:MA-SFP0': 'S15-274',
            'SI-11M2:MA-SFP0': 'S15-135',
            'SI-15M1:MA-SFP0': 'S15-043',
            'SI-15M2:MA-SFP0': 'S15-040',
            'SI-19M1:MA-SFP0': 'S15-258',
            'SI-19M2:MA-SFP0': 'S15-093',
        },
        'color': 'b'},
    'SDA1': {
        'current_str': '110',
        'sorting': {
            'SI-01C1:MA-SDA1': 'S15-138',
            'SI-04C4:MA-SDA1': 'S15-120',
            'SI-05C1:MA-SDA1': 'S15-195',
            'SI-08C4:MA-SDA1': 'S15-212',
            'SI-09C1:MA-SDA1': 'S15-207',
            'SI-12C4:MA-SDA1': 'S15-164',
            'SI-13C1:MA-SDA1': 'S15-100',
            'SI-16C4:MA-SDA1': 'S15-141',
            'SI-17C1:MA-SDA1': 'S15-223',
            'SI-20C4:MA-SDA1': 'S15-112',
        },
        'color': 'g'},
    'SFA1': {
        'current_str': '130',
        'sorting': {
            'SI-01C1:MA-SFA1': 'S15-142',
            'SI-04C4:MA-SFA1': 'S15-219',
            'SI-05C1:MA-SFA1': 'S15-102',
            'SI-08C4:MA-SFA1': 'S15-286',
            'SI-09C1:MA-SFA1': 'S15-236',
            'SI-12C4:MA-SFA1': 'S15-266',
            'SI-13C1:MA-SFA1': 'S15-265',
            'SI-16C4:MA-SFA1': 'S15-272',
            'SI-17C1:MA-SFA1': 'S15-098',
            'SI-20C4:MA-SFA1': 'S15-105',
        },
        'color': 'r'},
    'SDB1': {
        'current_str': '90',
        'sorting': {
            'SI-01C4:MA-SDB1': 'S15-168',
            'SI-02C1:MA-SDB1': 'S15-181',
            'SI-03C4:MA-SDB1': 'S15-174',
            'SI-04C1:MA-SDB1': 'S15-128',
            'SI-05C4:MA-SDB1': 'S15-146',
            'SI-06C1:MA-SDB1': 'S15-268',
            'SI-07C4:MA-SDB1': 'S15-139',
            'SI-08C1:MA-SDB1': 'S15-202',
            'SI-09C4:MA-SDB1': 'S15-244',
            'SI-10C1:MA-SDB1': 'S15-242',
            'SI-11C4:MA-SDB1': 'S15-149',
            'SI-12C1:MA-SDB1': 'S15-124',
            'SI-13C4:MA-SDB1': 'S15-107',
            'SI-14C1:MA-SDB1': 'S15-189',
            'SI-15C4:MA-SDB1': 'S15-188',
            'SI-16C1:MA-SDB1': 'S15-177',
            'SI-17C4:MA-SDB1': 'S15-186',
            'SI-18C1:MA-SDB1': 'S15-126',
            'SI-19C4:MA-SDB1': 'S15-123',
            'SI-20C1:MA-SDB1': 'S15-170',
        },
        'color': 'k'},
    'SFB1': {
        'current_str': '150',
        'sorting': {
            'SI-01C4:MA-SFB1': 'S15-104',
            'SI-02C1:MA-SFB1': 'S15-080',
            'SI-03C4:MA-SFB1': 'S15-061',
            'SI-04C1:MA-SFB1': 'S15-067',
            'SI-05C4:MA-SFB1': 'S15-068',
            'SI-06C1:MA-SFB1': 'S15-034',
            'SI-07C4:MA-SFB1': 'S15-060',
            'SI-08C1:MA-SFB1': 'S15-081',
            'SI-09C4:MA-SFB1': 'S15-156',
            'SI-10C1:MA-SFB1': 'S15-257',
            'SI-11C4:MA-SFB1': 'S15-234',
            'SI-12C1:MA-SFB1': 'S15-182',
            'SI-13C4:MA-SFB1': 'S15-233',
            'SI-14C1:MA-SFB1': 'S15-169',
            'SI-15C4:MA-SFB1': 'S15-059',
            'SI-16C1:MA-SFB1': 'S15-275',
            'SI-17C4:MA-SFB1': 'S15-153',
            'SI-18C1:MA-SFB1': 'S15-052',
            'SI-19C4:MA-SFB1': 'S15-071',
            'SI-20C1:MA-SFB1': 'S15-065',
        },
        'color': 'y'},
    'SDP1': {
        'current_str': '90',
        'sorting': {
            'SI-02C4:MA-SDP1': 'S15-092',
            'SI-03C1:MA-SDP1': 'S15-017',
            'SI-06C4:MA-SDP1': 'S15-175',
            'SI-07C1:MA-SDP1': 'S15-271',
            'SI-10C4:MA-SDP1': 'S15-020',
            'SI-11C1:MA-SDP1': 'S15-050',
            'SI-14C4:MA-SDP1': 'S15-109',
            'SI-15C1:MA-SDP1': 'S15-012',
            'SI-18C4:MA-SDP1': 'S15-155',
            'SI-19C1:MA-SDP1': 'S15-227',
        },
        'color': 'b'},
    'SFP1': {
        'current_str': '150',
        'sorting': {
            'SI-02C4:MA-SFP1': 'S15-063',
            'SI-03C1:MA-SFP1': 'S15-260',
            'SI-06C4:MA-SFP1': 'S15-180',
            'SI-07C1:MA-SFP1': 'S15-176',
            'SI-10C4:MA-SFP1': 'S15-250',
            'SI-11C1:MA-SFP1': 'S15-209',
            'SI-14C4:MA-SFP1': 'S15-165',
            'SI-15C1:MA-SFP1': 'S15-253',
            'SI-18C4:MA-SFP1': 'S15-229',
            'SI-19C1:MA-SFP1': 'S15-251',
        },
        'color': 'g'},
    'SDA2': {
        'current_str': '50',
        'sorting': {
            'SI-01C1:MA-SDA2': 'S15-248',
            'SI-04C4:MA-SDA2': 'S15-277',
            'SI-05C1:MA-SDA2': 'S15-245',
            'SI-08C4:MA-SDA2': 'S15-029',
            'SI-09C1:MA-SDA2': 'S15-256',
            'SI-12C4:MA-SDA2': 'S15-167',
            'SI-13C1:MA-SDA2': 'S15-031',
            'SI-16C4:MA-SDA2': 'S15-263',
            'SI-17C1:MA-SDA2': 'S15-166',
            'SI-20C4:MA-SDA2': 'S15-032',
        },
        'color': 'r'},
    'SFA2': {
        'current_str': '110',
        'sorting': {
            'SI-01C2:MA-SFA2': 'S15-282',
            'SI-04C3:MA-SFA2': 'S15-117',
            'SI-05C2:MA-SFA2': 'S15-021',
            'SI-08C3:MA-SFA2': 'S15-145',
            'SI-09C2:MA-SFA2': 'S15-220',
            'SI-12C3:MA-SFA2': 'S15-243',
            'SI-13C2:MA-SFA2': 'S15-171',
            'SI-16C3:MA-SFA2': 'S15-280',
            'SI-17C2:MA-SFA2': 'S15-281',
            'SI-20C3:MA-SFA2': 'S15-005',
        },
        'color': 'k'},
    'SDB2': {
        'current_str': '90',
        'sorting': {
            'SI-01C4:MA-SDB2': 'S15-197',
            'SI-02C1:MA-SDB2': 'S15-247',
            'SI-03C4:MA-SDB2': 'S15-218',
            'SI-04C1:MA-SDB2': 'S15-099',
            'SI-05C4:MA-SDB2': 'S15-211',
            'SI-06C1:MA-SDB2': 'S15-006',
            'SI-07C4:MA-SDB2': 'S15-235',
            'SI-08C1:MA-SDB2': 'S15-130',
            'SI-09C4:MA-SDB2': 'S15-226',
            'SI-10C1:MA-SDB2': 'S15-254',
            'SI-11C4:MA-SDB2': 'S15-162',
            'SI-12C1:MA-SDB2': 'S15-206',
            'SI-13C4:MA-SDB2': 'S15-096',
            'SI-14C1:MA-SDB2': 'S15-224',
            'SI-15C4:MA-SDB2': 'S15-140',
            'SI-16C1:MA-SDB2': 'S15-225',
            'SI-17C4:MA-SDB2': 'S15-129',
            'SI-18C1:MA-SDB2': 'S15-027',
            'SI-19C4:MA-SDB2': 'S15-222',
            'SI-20C1:MA-SDB2': 'S15-203',
        },
        'color': 'y'},
    'SFB2': {
        'current_str': '130',
        'sorting': {
            'SI-01C3:MA-SFB2': 'S15-121',
            'SI-02C2:MA-SFB2': 'S15-190',
            'SI-03C3:MA-SFB2': 'S15-192',
            'SI-04C2:MA-SFB2': 'S15-087',
            'SI-05C3:MA-SFB2': 'S15-210',
            'SI-06C2:MA-SFB2': 'S15-231',
            'SI-07C3:MA-SFB2': 'S15-158',
            'SI-08C2:MA-SFB2': 'S15-115',
            'SI-09C3:MA-SFB2': 'S15-008',
            'SI-10C2:MA-SFB2': 'S15-160',
            'SI-11C3:MA-SFB2': 'S15-019',
            'SI-12C2:MA-SFB2': 'S15-267',
            'SI-13C3:MA-SFB2': 'S15-078',
            'SI-14C2:MA-SFB2': 'S15-030',
            'SI-15C3:MA-SFB2': 'S15-090',
            'SI-16C2:MA-SFB2': 'S15-116',
            'SI-17C3:MA-SFB2': 'S15-018',
            'SI-18C2:MA-SFB2': 'S15-097',
            'SI-19C3:MA-SFB2': 'S15-179',
            'SI-20C2:MA-SFB2': 'S15-185',
        },
        'color': 'b'},
    'SDP2': {
        'current_str': '90',
        'sorting': {
            'SI-02C4:MA-SDP2': 'S15-252',
            'SI-03C1:MA-SDP2': 'S15-199',
            'SI-06C4:MA-SDP2': 'S15-088',
            'SI-07C1:MA-SDP2': 'S15-024',
            'SI-10C4:MA-SDP2': 'S15-079',
            'SI-11C1:MA-SDP2': 'S15-191',
            'SI-14C4:MA-SDP2': 'S15-025',
            'SI-15C1:MA-SDP2': 'S15-014',
            'SI-18C4:MA-SDP2': 'S15-161',
            'SI-19C1:MA-SDP2': 'S15-028',
        },
        'color': 'g'},
    'SFP2': {
        'current_str': '130',
        'sorting': {
            'SI-02C3:MA-SFP2': 'S15-062',
            'SI-03C2:MA-SFP2': 'S15-049',
            'SI-06C3:MA-SFP2': 'S15-194',
            'SI-07C2:MA-SFP2': 'S15-064',
            'SI-10C3:MA-SFP2': 'S15-237',
            'SI-11C2:MA-SFP2': 'S15-127',
            'SI-14C3:MA-SFP2': 'S15-057',
            'SI-15C2:MA-SFP2': 'S15-173',
            'SI-18C3:MA-SFP2': 'S15-089',
            'SI-19C2:MA-SFP2': 'S15-054',
        },
        'color': 'r'},
    'SDA3': {
        'current_str': '90',
        'sorting': {
            'SI-01C2:MA-SDA3': 'S15-217',
            'SI-04C3:MA-SDA3': 'S15-215',
            'SI-05C2:MA-SDA3': 'S15-035',
            'SI-08C3:MA-SDA3': 'S15-144',
            'SI-09C2:MA-SDA3': 'S15-216',
            'SI-12C3:MA-SDA3': 'S15-214',
            'SI-13C2:MA-SDA3': 'S15-204',
            'SI-16C3:MA-SDA3': 'S15-036',
            'SI-17C2:MA-SDA3': 'S15-051',
            'SI-20C3:MA-SDA3': 'S15-022',
        },
        'color': 'k'},
    'SDB3': {
        'current_str': '110',
        'sorting': {
            'SI-01C3:MA-SDB3': 'S15-084',
            'SI-02C2:MA-SDB3': 'S15-111',
            'SI-03C3:MA-SDB3': 'S15-228',
            'SI-04C2:MA-SDB3': 'S15-150',
            'SI-05C3:MA-SDB3': 'S15-198',
            'SI-06C2:MA-SDB3': 'S15-201',
            'SI-07C3:MA-SDB3': 'S15-196',
            'SI-08C2:MA-SDB3': 'S15-125',
            'SI-09C3:MA-SDB3': 'S15-183',
            'SI-10C2:MA-SDB3': 'S15-205',
            'SI-11C3:MA-SDB3': 'S15-047',
            'SI-12C2:MA-SDB3': 'S15-200',
            'SI-13C3:MA-SDB3': 'S15-037',
            'SI-14C2:MA-SDB3': 'S15-148',
            'SI-15C3:MA-SDB3': 'S15-058',
            'SI-16C2:MA-SDB3': 'S15-178',
            'SI-17C3:MA-SDB3': 'S15-255',
            'SI-18C2:MA-SDB3': 'S15-134',
            'SI-19C3:MA-SDB3': 'S15-083',
            'SI-20C2:MA-SDB3': 'S15-046',
        },
        'color': 'y'},
    'SDP3': {
        'current_str': '110',
        'sorting': {
            'SI-02C3:MA-SDP3': 'S15-042',
            'SI-03C2:MA-SDP3': 'S15-095',
            'SI-06C3:MA-SDP3': 'S15-055',
            'SI-07C2:MA-SDP3': 'S15-094',
            'SI-10C3:MA-SDP3': 'S15-011',
            'SI-11C2:MA-SDP3': 'S15-262',
            'SI-14C3:MA-SDP3': 'S15-136',
            'SI-15C2:MA-SDP3': 'S15-284',
            'SI-18C3:MA-SDP3': 'S15-137',
            'SI-19C2:MA-SDP3': 'S15-285',
        },
        'color': 'b'},
}


def get_family_string(serial):
    """."""
    fam_str = 'FAM1' if serial in family_1 else 'FAM2'
    return fam_str


def get_readme_file(fname):
    """."""
    with open(fname, 'r') as f:
        lines = f.readlines()
    data = {}
    for line in lines[3:]:
        serial, current, *multipoles = line.split()
        current = float(current)
        multipoles = [float(m) for m in multipoles]
        grad_curr_norm = multipoles[:len(multipoles)//2]
        grad_curr_skew = multipoles[len(multipoles)//2:]
        data[serial] = {
            'current': current,
            'grad_curr_norm': grad_curr_norm,
            'grad_curr_skew': grad_curr_skew, }
    return data


def get_readme_data():
    """."""
    currents = set()
    for data in fams.values():
        currents.add(data['current_str'])

    data = {}
    for fam_str in ('FAM1', 'FAM2'):
        data[fam_str] = dict()
        for current_str in currents:
            readme_fname = 'MULTIPOLES-{}-{}A.txt'.format(fam_str, current_str)
            # print(readme_fname)
            data[fam_str][current_str] = get_readme_file(readme_fname)
    return data


def update_families_data():
    """."""
    global fams
    readme_data = get_readme_data()
    for fam_name in fams:
        fam_data = fams[fam_name]
        fam_data['currents'] = dict()
        fam_data['grad_curr_norm'] = dict()
        fam_data['grad_curr_skew'] = dict()
        sorting = fam_data['sorting']
        # print(sorting)
        for magnet, serial in sorting.items():
            fam_str = get_family_string(serial)
            current_str = fam_data['current_str']
            data = readme_data[fam_str][current_str][serial]
            # print(data)
            fam_data['currents'][serial] = data['current']
            fam_data['grad_curr_norm'][serial] = data['grad_curr_norm']
            fam_data['grad_curr_skew'][serial] = data['grad_curr_skew']


def calc_magnetic_center(norm, skew):
    """."""
    a0 = skew[0]
    b0 = norm[0]
    a1 = skew[1]
    b1 = norm[1]
    D = b0 + a0 * 1j
    Q = b1 + a1 * 1j
    if multipole_index == 2:
        a2 = skew[2]
        b2 = norm[2]
        S = b2 + a2 * 1j
        z0 = -Q/S/2.0
    elif multipole_index == 1:
        z0 = -D/Q
    xcenter = 1e6 * z0.real
    ycenter = 1e6 * z0.imag
    return xcenter, ycenter


def plot_parameter(param):
    """."""

    def plot_fam(serials, fam_label):
        fam_data = fams[fam_label]
        current_str = fam_data['current_str']
        sorting = fam_data['sorting']
        currents = fam_data['currents']
        grad_curr_norm = fam_data['grad_curr_norm']
        grad_curr_skew = fam_data['grad_curr_skew']
        mult_norm, mult_skew = [], []
        xcenters, ycenters = [], []
        roll_error = []
        for magnet, serial in sorting.items():
            g_norm = grad_curr_norm[serial]
            g_skew = grad_curr_skew[serial]
            current = currents[serial]
            mult_norm.append(g_norm[multipole_index])
            mult_skew.append(g_skew[multipole_index])
            xcenter, ycenter = calc_magnetic_center(g_norm, g_skew)
            xcenters.append(xcenter), ycenters.append(ycenter)
            bx_by = g_skew[multipole_index] / g_norm[multipole_index]
            merror = 1000 * np.arctan(bx_by) / (1 + multipole_index)
            roll_error.append(merror)
        serial = list(sorting.values())
        color = fam_data['color']
        m_avg, m_std, m_ptp = \
            np.mean(mult_norm), np.std(mult_norm), np.ptp(mult_norm)
        m_dif = 100*(mult_norm - m_avg)/m_avg
        x_avg, x_std, x_ptp = \
            np.mean(xcenters), np.std(xcenters), np.ptp(xcenters)
        y_avg, y_std, y_ptp = \
            np.mean(ycenters), np.std(ycenters), np.ptp(ycenters)
        r_avg, r_std, r_ptp = \
            np.mean(roll_error), np.std(roll_error), np.ptp(roll_error)
        sfmt = (
            '{} | {:+8.3f} A | {:+.4f} ± {:.5f} {:.5f} [((T/m).A] |'
            ' {:+5.1f} ± {:5.1f} {:5.1f} um | {:+5.1f} ± {:5.1f} {:5.1f} um |'
            ' {:+.3f} ± {:.3f} {:.3f} [mrad]')
        print(sfmt.format(fam_label, float(current_str),
                          m_avg, m_std, m_ptp, x_avg, x_std, x_ptp,
                          y_avg, y_std, y_ptp, r_avg, r_std, r_ptp))
        if param == 'm':
            plt.plot(len(serials) + np.arange(len(serial)), m_dif, color + '-')
            plt.plot(len(serials) + np.arange(len(serial)), m_dif, color + 'o',
                    label=fam_label)
        elif param == 'x':
            plt.plot(len(serials) + np.arange(len(serial)), xcenters, color + '-')
            plt.plot(len(serials) + np.arange(len(serial)), xcenters, color + 'o',
                     label=fam_label)
        elif param == 'y':
            plt.plot(len(serials) + np.arange(len(serial)),
                     ycenters, color + '-')
            plt.plot(len(serials) + np.arange(len(serial)), ycenters, color + 'o',
                     label=fam_label)
        elif param == 'r':
            plt.plot(len(serials) + np.arange(len(serial)),
                     roll_error, color + '-')
            plt.plot(len(serials) + np.arange(len(serial)), roll_error, color + 'o',
                     label=fam_label)
        serials += serial
        return serials

    serials = []
    serials = plot_fam(serials, 'SDA0')
    serials = plot_fam(serials, 'SFA0')
    serials = plot_fam(serials, 'SDB0')
    serials = plot_fam(serials, 'SFB0')
    serials = plot_fam(serials, 'SDP0')
    serials = plot_fam(serials, 'SFP0')
    serials = plot_fam(serials, 'SDA1')
    serials = plot_fam(serials, 'SFA1')
    serials = plot_fam(serials, 'SDB1')
    serials = plot_fam(serials, 'SFB1')
    serials = plot_fam(serials, 'SDP1')
    serials = plot_fam(serials, 'SFP1')
    serials = plot_fam(serials, 'SDA2')
    serials = plot_fam(serials, 'SFA2')
    serials = plot_fam(serials, 'SDB2')
    serials = plot_fam(serials, 'SFB2')
    serials = plot_fam(serials, 'SDP2')
    serials = plot_fam(serials, 'SFP2')
    serials = plot_fam(serials, 'SDA3')
    serials = plot_fam(serials, 'SDB3')
    serials = plot_fam(serials, 'SDP3')

    plt.xlabel('Magnet Index')
    if param == 'm':
        plt.ylabel('Relative Error [%]')
        plt.title('Integrated Sextupole Relative Error of S15 Magnets')
    elif param == 'x':
        plt.ylabel('X [um]')
        plt.title('Horizontal Magnetic Center of S15 Magnets')
    elif param == 'y':
        plt.ylabel('Y [um]')
        plt.title('Vertical Magnetic Center of S15 Magnets')
    elif param == 'r':
        plt.ylabel('Error [mrad]')
        plt.title('Roll Angle Error of S15 Magnets')
    # plt.xticks(np.arange(len(serials)), serials, rotation='vertical')
    plt.legend(ncol=5)
    plt.grid()
    plt.show()


update_families_data()
plot_parameter('m')
# plot_parameter('x')
# plot_parameter('y')
# plot_parameter('r')
