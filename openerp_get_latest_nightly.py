

import tarfile
import os
import shutil


def download_latest_nightly():
    """
    Pulls the latest nightly from OpenERP server
    """

    url = "http://nightly.openerp.com/6.1/nightly/src/openerp-6.1-latest.tar.gz"
    #url = "http://192.168.2.149:5555/openerp-nightly.tar.gz"

    print "Starting to download the archive..."

    os.system("wget " + url)

    #nightly = urllib2.urlopen(url)
    #data = nightly.read()
    #with open("latest.tar.gz", "wb") as code:
        #code.write(data)

    print "Finished downloading the archive..."


def untar_archive():
    """
    Untar the archive downloaded, in current path and name latest.tar.gz
    """

    print "Untaring the archive..."

    tar = tarfile.open("openerp-6.1-latest.tar.gz")
    tar.extractall()
    tar.close()


def copy_addons(nightly_directory, addons_directory):
    """
    Copy addons from latest version over the old ones
    """

    print "Copying addons directory..."

    cp_cmd = "/bin/cp -rf " + nightly_directory + " " + addons_directory
    os.system(cp_cmd)


def chown_addons(addons_directory):
    """
    Ensures that all the new files belong to openerp:openerp
    """

    print "Chowning..."

    os.system('chown -R openerp:openerp ' + addons_directory)


def restart_openerp():
    """
    Restarts the openerp service
    """

    print "Restarting OpenERP..."
    os.system('service openerp-server restart')


def cleanup():
    """
    Removes the tar and the extracted folder
    """

    print "Cleaning up..."
    os.system('rm openerp-6.1-latest.tar.gz')
    os.system('rm -rf openerp-6.1-*/')



if __name__ == "__main__":

    #modify to fit the addons path
    addons_directory = "/opt/openerp/server/openerp/addons/"
    
    nightly_directory = "openerp-6.1-*/openerp/addons/"

    download_latest_nightly()
    untar_archive()
    copy_addons(nightly_directory, addons_directory)
    chown_addons(addons_directory)
    cleanup()
    restart_openerp()