from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer as ModbusRtuFramer
import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

UNIT = 0x1

#modbusTCP = ModbusClient('localhost', port=5020)
#modbusTCPRTU = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
modbusBinary = ModbusClient(method='binary', port='COM1', timeout=1)
modbusASCII = ModbusClient(method='ascii', port='COM1', timeout=1)
modbusRTU = ModbusClient(method='rtu', port='COM1', timeout=1, baudrate=9600)

def run_sync_client():
    client = modbusRTU
    client.connect()
    """log.debug("Reading Coils")
    rr = client.read_coils(1, 1, unit=UNIT)
    log.debug(rr)"""
    log.debug("Write to multiple holding registers and read back")
    rq = client.write_registers(1, [10] * 8, unit=UNIT)
    rr = client.read_holding_registers(1, 8, unit=UNIT)
    assert (not rq.isError())  # test that we are not an error
    assert (rr.registers == [10] * 8)  # test the expected value
    #client.send(b'0x1 0x3 0x0 0x1 0x0 0x8 0x15 0xcc')

if __name__ == "__main__":
    run_sync_client()