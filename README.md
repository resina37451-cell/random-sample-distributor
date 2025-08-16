# Sample Distributor

## Description

The **Sample Distributor** is a Python tool that allows you to divide a set of numbered samples into groups randomly and redistribute them into subgroups through multiple stages. It's ideal for scientific experiments, statistical studies, or any situation where you need to randomize and group data in a controlled manner.

## Features

- 🎲 **Random distribution**: Divides numbered samples into groups randomly
- 📊 **Multiple stages**: Allows up to 4 redistribution stages
- 🏷️ **Custom naming**: Define custom names for groups and variables
- 🔄 **Flexible redistribution**: Each group can be divided into 2 subgroups with specific names
- 📋 **Clear visualization**: Shows current distribution at each stage

## Prerequisites

- Python 3.6 or higher
- `random` library (included in Python standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/sample-distributor.git
cd sample-distributor
```

2. Run the program:
```bash
python sample_distributor.py
```

## How to Use

### Usage Example

1. **Run the program:**
```bash
python sample_distributor.py
```

2. **Enter the total number of samples:**
```
Enter the total number of samples: 12
```

3. **Define the number of initial groups:**
```
Enter the number of groups: 3
```

4. **Name each group:**
```
Enter the name of group 1: Control
Enter the name of group 2: Treatment A
Enter the name of group 3: Treatment B
```

5. **The program will show the initial distribution:**
```
Stage 1 completed. Groups:
Control: [1, 4, 7, 10]
Treatment A: [2, 5, 8, 11]
Treatment B: [3, 6, 9, 12]
```

6. **Choose whether to redistribute and define variables:**
```
Do you want to distribute the samples again? (Y/N): Y
Enter the name of variable 1 for stage 2: Low Dose
Enter the name of variable 2 for stage 2: High Dose
```

### Workflow

The program follows this flow:
1. **Initial input**: Define number of samples and groups
2. **Distribution**: Divide samples randomly
3. **Visualization**: Show formed groups
4. **Redistribution** (optional): Each group is divided into 2 subgroups
5. **Repetition**: Process can be repeated up to 4 stages

## Code Structure

```
sample_distributor.py
├── dividir_amostras()     # Function for random division
├── redistribuir_grupos()  # Function for redistribution
└── main()                # Main function with interface
```

## Technologies Used

- **Python 3.x**
- **random library** - For sample randomization

## Example Output

```
Stage 1 completed. Groups:
Control: [2, 5, 8, 11]
Treatment A: [1, 4, 7, 10]
Treatment B: [3, 6, 9, 12]

Stage 2 completed. Groups:
Control - Low Dose: [2, 8]
Control - High Dose: [5, 11]
Treatment A - Low Dose: [1, 7]
Treatment A - High Dose: [4, 10]
Treatment B - Low Dose: [3, 9]
Treatment B - High Dose: [6, 12]
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@your_username](https://github.com/your-username)

Project Link: [https://github.com/your-username/sample-distributor](https://github.com/your-username/sample-distributor)

## Project Status

✅ **Version 1.0** - Basic functionality implemented
- Random sample distribution
- Redistribution in up to 4 stages
- Command line interface

### Upcoming Features
- [ ] CSV export
- [ ] Graphical interface
- [ ] Configuration saving
- [ ] Support for more than 4 stages
