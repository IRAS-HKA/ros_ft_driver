import rospy
import subprocess
from ftn_axia80.srv import userbias

#TODO Set IP in config and use as rosparameter
def handle_req(req):
    try:
        subprocess.run(f'wget http://192.168.1.220/rundata.cgi?cmd=setuserbias -o ./temp && rm ./temp', shell = True, check = True, text = True)
        rospy.loginfo('Set user bias successful')
        return True
    except:
        rospy.logerr('Set user bias failed!')
        return False

if __name__ == '__main__':
    rospy.init_node("ftn_axia_set_userbias_service")
    s = rospy.Service("ftn_axia/set_userbias", userbias, handle_req)
    rospy.spin()