    # ! python2.7
#--------------------------- Launch.py ----------------------------------------
# |   Time   | Version | Contributor | Comment
# | 2017.8.2 |  1.0    | H.F.        |
#------------------------------------------------------------------------------

from Sensor.SHT31 import*
import multiprocessing

#--------------------------  I2C setting --------------------------------------
#i2c-3   i2c             i2c-1-mux (chan_id 0)                   I2C adapter
#i2c-1   i2c             bcm2835 I2C adapter                     I2C adapter
#i2c-8   i2c             i2c-1-mux (chan_id 5)                   I2C adapter
#i2c-6   i2c             i2c-1-mux (chan_id 3)                   I2C adapter
#i2c-4   i2c             i2c-1-mux (chan_id 1)                   I2C adapter
#i2c-9   i2c             i2c-1-mux (chan_id 6)                   I2C adapter
#i2c-10  i2c             i2c-1-mux (chan_id 7)                   I2C adapter
#i2c-7   i2c             i2c-1-mux (chan_id 4)                   I2C adapter
#i2c-5   i2c             i2c-1-mux (chan_id 2)                   I2C adapter
#------------------------------------------------------------------------------


# Box channel
box1top = SHT31(3,'Top','30%')
box1bot = SHT31(3,'Bottom','30%')
box2top = SHT31(4,'Top','60%')
box2bot = SHT31(4,'Bottom','60%')
box3top = SHT31(5,'Top','90%')
box3bot = SHT31(5,'Bottom','90%')

PC30 = SHT31(6,'Top','30%PC')
PC60 = SHT31(7, 'Top','60%PC')


# multiprocessing
if __name__ == '__main__':

    p_box1top = multiprocessing.Process(target = box1top.record, args = ())
    p_box1bot = multiprocessing.Process(target = box1bot.record, args = ())
    p_box2top = multiprocessing.Process(target = box2top.record, args = ())
    p_box2bot = multiprocessing.Process(target = box2bot.record, args = ())
    p_box3top = multiprocessing.Process(target = box3top.record, args = ())
    p_box3bot = multiprocessing.Process(target = box3bot.record, args = ())
    #p_env = multiprocessing.Process(target = env.record, args = ())
    p_PC30 = multiprocessing.Process(target = PC30.record, args = ())
    p_PC60 = multiprocessing.Process(target = PC60.record, args = ())

    p_box1top.start()
    p_box1bot.start()
    p_box2top.start()
    p_box2bot.start()
    p_box3top.start()
    p_box3bot.start()
    #p_env.start()
    p_PC30.start()
    p_PC60.start()


############## To Do: Pool ############################
#    p = Pool(4)
#    p.apply_async(box1up.record, args=())
#    p.apply_async(box1down.record,args=())
#    p.close
#    p.join
