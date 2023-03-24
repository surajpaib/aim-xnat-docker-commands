#!/usr/bin/env python
import argparse
import os
import xnat
from loguru import logger

def main():
    #######################################################
    # PARSE INPUT ARGS
    parser = argparse.ArgumentParser(description='Add metadata')
    parser.add_argument('uri', help='Object URI')
    parser.add_argument('xnat_host', help='XNAT Host')
    parser.add_argument('xnat_user', help='XNAT Username')
    parser.add_argument('xnat_pass', help='XNAT Password')
    args=parser.parse_args()


    #######################################################
    # CONNECT TO XNAT
    #######################################################

    logger.info("Connecting to XNAT {}.".format(args.xnat_host))
    xnat_session = xnat.connect(args.xnat_host, user=args.xnat_user, password=args.xnat_pass)


    #######################################################
    # GET OBJECT FROM URI
    #######################################################
    logger.info("Getting object from URI {}.".format(args.uri))
    obj = xnat_session.create_object(args.uri.replace("archive", "data"))

    #######################################################
    # UPDATE METADATA
    #######################################################

    logger.info("Updating metadata.")
    obj.set("xnat:ctScanData/bodyPartExamined", "HEAD")

    logger.info("Done.")
    
if __name__ == '__main__':
    main()
