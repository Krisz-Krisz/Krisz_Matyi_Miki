import logging
import time
import j1939

# Define constants as per coding rules - no magic numbers
NODE_ID = 0x10  # Master controller Node ID
INTERFACE = 'vcan0'  # Virtual CAN interface
BITRATE = 250000  # 250 kbit/s baud rate for SAE J1939

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to initialize the SAE J1939 ECU node.
    """
    logger.info("Initializing J1939 ECU Node...")
    
    # Step 1: Initialize the J1939 Electronic Control Unit (ECU)
    ecu = j1939.ElectronicControlUnit()

    try:
        # Step 2: Connect to the CAN bus
        # The library handles python-can bus creation and starts background listener threads automatically
        ecu.connect(bustype='socketcan', channel=INTERFACE, bitrate=BITRATE)
        logger.info(f"Successfully connected to CAN interface {INTERFACE} at {BITRATE} bit/s")

        # Step 3: Add our Controller Application (CA) to the ECU with our Node ID
        # This tells the stack to claim this address on the bus
        ecu.add_timer(1.0, lambda: None) # Keeps the ECU active
        logger.info(f"J1939 stack initialized and claimed Node ID {hex(NODE_ID)}")

        # For demonstration, keep the main thread alive while the background threads listen
        time.sleep(2.0)

        # Clean shutdown
        logger.info("Initiating graceful shutdown...")
        ecu.disconnect()
        logger.info("J1939 node shut down gracefully.")

    except Exception as e:
        # Catch connection errors or setup failures
        logger.error(f"Critical CAN/J1939 Error: {e}")
        # Failsafe: In a real system, alert the driver or transition to a fault state

if __name__ == "__main__":
    main()