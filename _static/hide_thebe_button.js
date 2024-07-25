(function() {
    // List of filenames for which the Thebe button should be hidden
    const filenamesToHideButton = [
        'additional_exercises.html',
        'analysis_task_1.html',
        'analysis_task_2.html',
        'analysis_task_3html',
        'analysis_task_intro.html',
        'control_flow.html',
        'dictionaries.html',
        'functions.html',
        'fundamentals.html',
        'imports.html',
        'lists.html',
        'loops.html',
        'motivation.html',
        'recap.html',
        'basic_commands.html',
        'control_flow.html',
        'data_types.html',
        'gettingstarted.html',
        'good_practise.html',
        'load_data.html',
        'manipulating_data.html',
        'plots.html',
        'stats.html',
        'regression_analysis_with_r_extras.html',
        'hypothesis_testing.html',
        'introduction_to_regression.html',
        'logistic_regression.html',
        'multiple_linear_regression.html',
        'regression_analysis_with_r_summary.html',
        'advanced_regression_analysis_with_R_extras.html',
        'advanced_regression_analysis_with_R_summary.html',
        'expanding_the_mixed_effects_model_framework.html',
        'mixed_effects_models.html',
        'regression_models_with_interaction_terms.html'
    ];

    // Function to get the current page's filename
    function getCurrentFilename() {
        const url = window.location.pathname;
        const filename = url.substring(url.lastIndexOf('/') + 1);
        return filename;
    }

    // Function to add the custom CSS to the document
    function addCustomCSS() {
        const css = `
            .dropdown.dropdown-launch-buttons {
                display: none !important;
            }
        `;
        const style = document.createElement('style');
        style.type = 'text/css';
        style.appendChild(document.createTextNode(css));
        document.head.appendChild(style);
    }

    // Main function to check the filename and apply CSS if needed
    function applyCSSIfNeeded() {
        const currentFilename = getCurrentFilename();
        if (filenamesToHideButton.includes(currentFilename)) {
            addCustomCSS();
        }
    }

    // Run the main function when the page loads
    window.onload = applyCSSIfNeeded;
})();
