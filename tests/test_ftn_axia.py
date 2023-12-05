from ftn_axia.ftn_axia import FtnAxia
import math


def test_read_ft():
    my_sensor = FtnAxia()
    data_ft = bytearray.fromhex("12340000044efe80f185fad3e8d60177")
    data_calinfo = bytearray.fromhex("12340203000F4240000F42403b9c3b9c6b4b026302630263")
    my_sensor._process_read_calibration_info_bytes(data_calinfo)
    my_sensor._process_read_ft_bytes(data_ft)

    assert my_sensor.Fx_raw == 1102
    assert my_sensor.Fy_raw == -384
    assert my_sensor.Fz_raw == -3707
    assert my_sensor.Tx_raw == -1325
    assert my_sensor.Ty_raw == -5930
    assert my_sensor.Tz_raw == 375

    assert math.isclose(my_sensor.Fx_cal, 16.82, rel_tol=0.01)
    assert math.isclose(my_sensor.Fy_cal, -5.86, rel_tol=0.01)
    assert math.isclose(my_sensor.Fz_cal, -101.8, rel_tol=0.01)
    assert math.isclose(my_sensor.Tx_cal, -0.8096, rel_tol=0.01)
    assert math.isclose(my_sensor.Ty_cal, -3.623, rel_tol=0.01)
    assert math.isclose(my_sensor.Tz_cal, 0.2291, rel_tol=0.01)


def test_read_calibration_info():
    my_sensor = FtnAxia()
    data = bytearray.fromhex("12340203000F4240000F42403b9c3b9c6b4b026302630263")
    my_sensor._process_read_calibration_info_bytes(data)

    assert my_sensor.forceUnits == 2
    assert my_sensor.torqueUnits == 3
    assert my_sensor.countsPerForce == 1000000
    assert my_sensor.countsPerTorque == 1000000
    assert my_sensor.sf0 == 15260
    assert my_sensor.sf1 == 15260
    assert my_sensor.sf2 == 27467
    assert my_sensor.sf3 == 611
    assert my_sensor.sf4 == 611
    assert my_sensor.sf5 == 611


def test_write_transform():
    my_sensor = FtnAxia()
    cmd = my_sensor._config_command_write_transform(dunits=3, runits=1, dx=0, dy=0, dz=1, rx=0, ry=0, rz=180)
    assert cmd == bytearray.fromhex("0203010000000000640000000046500000000000")     # Fehler in Dokumentation?


def test_write_threshold():
    my_sensor = FtnAxia()
    data = bytearray.fromhex("12340203000F4240000F42403b9c3b9c6b4b026302630263")
    my_sensor._process_read_calibration_info_bytes(data)
    cmd = my_sensor._config_command_write_threshold(index=2, axis=0, outputCode=16, comparison=-1, compareValue=488320)
    # was genau ist der outputCode?
    assert cmd == bytearray.fromhex("03020010FF002000000000000000000000000000")
