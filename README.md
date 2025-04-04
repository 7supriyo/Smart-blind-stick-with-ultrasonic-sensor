

# Smart Blind Stick with Ultrasonic Sensor

## Project Overview

This project aims to develop an affordable and efficient smart blind stick designed to aid visually impaired individuals in navigating their surroundings safely and independently. The smart blind stick utilizes ultrasonic sensors to detect obstacles within a range of up to 2 meters and provides feedback to the user in multiple forms to alert them of nearby obstacles.

## Features

- **Auditory Feedback through Buzzer Tones:** The stick is equipped with a piezo buzzer that emits different tones based on the distance of the detected obstacle. The tones vary in frequency and duration, providing a clear indication of the proximity of the obstacle.
- **Haptic Feedback via Vibration Motor:** The stick includes a vibration motor that provides haptic feedback, particularly useful in noisy environments. The vibration intensity changes based on the distance to the obstacle.
- **Three-Level Proximity Alerts:** The system categorizes obstacles into three proximity levels (far, medium, near) and triggers specific feedback patterns accordingly.

## Components Used

- **Raspberry Pi Pico (Microcontroller):** Serves as the main controller, processing input from the ultrasonic sensors and controlling the buzzer and vibration motor.
- **HC-SR04 Ultrasonic Sensor:** Used for measuring distances and detecting obstacles.
- **Piezo Buzzer (5V):** Provides auditory feedback to the user.
- **Vibration Motor (3V):** Provides haptic feedback to the user.


## Applications

- **Independent Navigation for Visually Impaired:** Assists visually impaired individuals in navigating their surroundings independently.
- **Obstacle Detection in Indoor/Outdoor Environments:** Effective in both indoor and outdoor environments for detecting obstacles.
- **Low-Cost Alternative to Commercial Solutions:** Offers a cost-effective alternative to commercially available navigation aids.

## Circuit Design

### Schematic Diagram

![Complete circuit schematic](![Screenshot 2025-03-29 133621](https://github.com/user-attachments/assets/5afb2840-12b6-40f8-a708-c21f126a45c4)
)

### Component Connections

| Component            | Pico Pin | Function         |
|----------------------|----------|------------------|
| Ultrasonic 1 (TRIG)  | GP3      | Trigger pulse    |
| Ultrasonic 1 (ECHO)  | GP2      | Echo reception   |
| Buzzer               | GP19     | Audio alerts     |
| Vibration Motor      | GP18     | Haptic feedback  |
| Power Switch         | GP20     | System control   |





### Algorithm Flow

1. Send 10µs trigger pulse.
2. Measure echo pulse duration.
3. Calculate distance (cm).
4. Activate alerts based on distance thresholds.
5. Repeat every 100ms.

## Testing & Results

### Performance Metrics

The performance of the smart blind stick was evaluated based on the distance detected by the ultrasonic sensor and the corresponding responses from the buzzer and vibration motor.

| Distance (cm) | Buzzer Frequency | Motor State |
|---------------|------------------|-------------|
| >50           | Off              | Off         |
| 30-50         | 500Hz            | Pulsed      |
| <30           | 800Hz            | Continuous  |

### Simulation Results

![Wokwi simulation output](![Screenshot 2025-03-29 155413](https://github.com/user-attachments/assets/7e2091f2-2168-43bb-aab7-bf81c3b0a1e9)
)

## Conclusion

The implemented system successfully detects obstacles within a 2m range with ±2cm accuracy. Future improvements include:

- Waterproof casing
- Bluetooth connectivity
- AI-based object recognition

## References

1. Raspberry Pi Foundation, "Raspberry Pi Pico Datasheet," [Online]. Available: https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf. [Accessed: Mar. 29, 2025].
2. HC-SR04 Ultrasonic Sensor Technical Manual, [Online]. Available: https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf. [Accessed: Mar. 29, 2025].
3. MicroPython Documentation, [Online]. Available: https://docs.micropython.org/en/latest/. [Accessed: Mar. 29, 2025].


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to customize the README further to suit the specifics of your project and repository.
