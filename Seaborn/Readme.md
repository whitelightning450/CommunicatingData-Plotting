## 🎨 Seaborn: A High-Level Statistical Data Visualization Library

**Seaborn** is a powerful Python library built on top of Matplotlib, designed to create informative and attractive statistical graphics. It focuses on visualizing the relationships between data variables, especially when dealing with data organized in Pandas DataFrames.
This module has been adapted from the libraries GitHub page, [Seaborn](https://github.com/mwaskom/seaborn).

### Key Features of Seaborn

* **Statistical Focus:** Seaborn is optimized for statistical visualization, automatically handling complex tasks like estimating and plotting linear regression models, confidence intervals, and distributions.
* **High-Level API:** It offers a concise, high-level interface that allows you to create sophisticated, multi-layered plots with a single function call, reducing the amount of code compared to raw Matplotlib.
* **Aesthetics and Themes:** Seaborn comes with modern default themes and color palettes that make plots look professional and visually appealing out-of-the-box.
* **Pandas Integration:** It works natively with Pandas DataFrames, using column names directly for plot mapping (e.g., `x='Temperature'`, `y='Sales'`), streamlining visualization workflows.
* **Complex Plot Types:** It simplifies the creation of specialized plots essential for statistical analysis, such as violin plots, joint plots (combining scatter plots and histograms), and pair plots (matrix of all variable relationships).

---

## 🆚 Matplotlib vs. Seaborn

While Seaborn builds upon Matplotlib, they serve different primary purposes, making them complementary tools in the Python data science ecosystem.

| Feature | Matplotlib | Seaborn |
| :--- | :--- | :--- |
| **Abstraction Level** | **Low-level** (The "Engine"). Requires detailed control over every element (axes, figures, lines). | **High-level** (The "Driver"). Provides easy-to-use function wrappers for complex statistical plots. |
| **Primary Focus** | General-purpose plotting (lines, bars, images, 3D plots). | Specialized statistical data visualization and relationship exploration. |
| **Data Input** | Primarily requires NumPy arrays or Python sequences for X and Y coordinates. | Primarily accepts Pandas DataFrames and uses column names for mapping. |
| **Aesthetics/Themes**| Default plots are basic and require manual styling (e.g., color, font, grid). | Automatically applies appealing, modern themes and color palettes. |
| **Complex Plots** | Requires significant code (e.g., multiple subplots, statistical lines, legend management) to create distributions. | Single function calls for complex statistical plots like `sns.scatterplot()`, `sns.jointplot()`, or `sns.histplot()`. |
| **Relationship** | Seaborn is a **wrapper** and **extension** of Matplotlib. | Seaborn depends on Matplotlib for underlying rendering. You can use Matplotlib functions to fine-tune Seaborn plots. |

### Conclusion

* Use **Matplotlib** when you need ultimate control, custom layouts, or specialized plots like embedding images, generating 3D surfaces, or drawing simple lines/bars where data relationships aren't the focus.
* Use **Seaborn** when your goal is to quickly and effectively visualize the **statistical relationships** within your data using professional, predefined aesthetics.

We will focus on the following sections for our workshop, which will cover more than plotting methods, such as statistical analysis, distributions, error, and regression:
* [Module 1: Introduction](./Mod1-introduction.ipynb)
* [Module 2: Overview of Seaborn plotting functions](./Mod2-function_overview.ipynb)
* [Module 3: Data Structures Accepted by Seaborn](./Mod3-data_structure.ipynb)
* [Module 4: Visualizing Statistical Relationships](./Mod4-relational.ipynb)
* [Module 5: Visualizing Data Distributions](./Mod5-distributions.ipynb)
* [Module 6: Visualizing Categorical Data](./Mod6-categorical.ipynb)
* [Module 7: Multiplot Grids](./Mod7-axis_grids.ipynb)
* [Module 8: Regression Fits](./Mod9-regression.ipynb)

