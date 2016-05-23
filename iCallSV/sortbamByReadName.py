"""
Created on Mar 18, 2015
Description: This module will sort bam file by name
@author: Ronak H Shah
"""

import os
import sys
import pysam
import logging


def sortBam(inputBam, outputBamName, outputDir):
    logger = logging.getLogger(__name__)
    logger.info("sortbamByReadName: Trying to sort BAM file by Read Name")
    if(os.path.isdir(outputDir)):
        logger.info("sortbamByReadName: The output directory %s exists", outputDir)
        outputFile = outputDir + "/" + outputBamName
    else:
        logger.info("sortbamByReadName: The output directory %s does not exists !!", outputDir)
        sys.exit()

    if(os.path.isfile(inputBam)):
        try:
            pysam.sort("-n", inputBam, outputFile)
        except IndexError as err:
            exception = "Index error({0}): {1}".format(err.errno, err.strerror)
            logger.info("%s", exception)
        except IOError as err:
            exception = "I/O error({0}): {1}".format(err.errno, err.strerror)
            logger.info("%s", exception)
    else:
        logger.info("sortbamByReadName:Bam File %s does not exists !!", inputBam)
        sys.exit()
    logger.info("sortbamByReadName: Finished sorting BAM file by Read Name.")
    return(outputFile)

#sortBam('/home/shahr2/M15-2555.recal.bam', "M15-2555.recal.NSORT","/home/shahr2/")
