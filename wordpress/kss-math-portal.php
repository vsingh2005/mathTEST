<?php
/**
 * Plugin Name: KSS Math Portal & Question Bank Manager
 * Plugin URI: https://kidsstemstudio.com/
 * Description: Integrates the Kids STEM Studio Math Placement Assessment Portal into WordPress. Features an Admin Panel Question Bank Editor, Color Scheme Customizer, Elementor Shortcodes, and REST API endpoints.
 * Version: 2.2.0
 * Author: Kids STEM Studio
 * Author URI: https://kidsstemstudio.com/
 * License: GPLv2 or later
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class KSS_Math_Portal_Plugin {

    public function __construct() {
        register_activation_hook(__FILE__, array($this, 'plugin_activate'));
        add_action('admin_menu', array($this, 'register_admin_menu'));
        add_action('rest_api_init', array($this, 'register_rest_routes'));

        // Elementor / Theme Shortcodes
        add_shortcode('kss_math_login', array($this, 'render_login_shortcode'));
        add_shortcode('kss_math_portal', array($this, 'render_portal_shortcode'));
        add_shortcode('kss_math_instructions', array($this, 'render_instructions_shortcode'));
        add_shortcode('kss_math_exam', array($this, 'render_exam_shortcode'));
        add_shortcode('kss_math_results', array($this, 'render_results_shortcode'));
        add_shortcode('kss_math_practice', array($this, 'render_practice_shortcode'));

        add_action('wp_enqueue_scripts', array($this, 'enqueue_frontend_assets'));
    }

    public function plugin_activate() {
        if (!get_option('kss_math_question_bank')) {
            $default_questions = $this->get_default_question_bank();
            update_option('kss_math_question_bank', json_encode($default_questions));
        }
        if (!get_option('kss_math_portal_settings')) {
            update_option('kss_math_portal_settings', json_encode($this->get_default_settings()));
        }
    }

    public function enqueue_frontend_assets() {
        wp_enqueue_style('dashicons');
    }

    public function register_admin_menu() {
        add_menu_page(
            'KSS Math Portal',
            'Math Portal',
            'manage_options',
            'kss-math-portal',
            array($this, 'render_admin_page'),
            'dashicons-calculator',
            30
        );
    }

    public function render_admin_page() {
        if (!current_user_can('manage_options')) {
            return;
        }

        $active_tab = isset($_GET['tab']) ? sanitize_text_field($_GET['tab']) : 'questions';

        $message = '';
        if (isset($_POST['kss_save_question'])) {
            check_admin_referer('kss_question_action', 'kss_nonce');
            $this->handle_save_question($_POST);
            $message = 'Question saved successfully!';
        } elseif (isset($_POST['kss_delete_question'])) {
            check_admin_referer('kss_question_action', 'kss_nonce');
            $this->handle_delete_question(intval($_POST['question_id']));
            $message = 'Question deleted successfully!';
        } elseif (isset($_POST['kss_reset_default_bank'])) {
            check_admin_referer('kss_question_action', 'kss_nonce');
            update_option('kss_math_question_bank', json_encode($this->get_default_question_bank()));
            $message = 'Question Bank reset to default template!';
        } elseif (isset($_POST['kss_save_settings'])) {
            check_admin_referer('kss_settings_action', 'kss_settings_nonce');
            $this->handle_save_settings($_POST);
            $message = 'Portal color theme and settings updated successfully!';
        }

        $raw_questions = get_option('kss_math_question_bank', '[]');
        $questions = json_decode($raw_questions, true) ?: array();

        $raw_settings = get_option('kss_math_portal_settings', '[]');
        $settings = array_merge($this->get_default_settings(), json_decode($raw_settings, true) ?: array());

        $edit_question = null;
        if (isset($_GET['action']) && $_GET['action'] === 'edit' && isset($_GET['id'])) {
            $edit_id = intval($_GET['id']);
            foreach ($questions as $q) {
                if ($q['id'] === $edit_id) {
                    $edit_question = $q;
                    break;
                }
            }
        }
        ?>
        <div class="wrap">
            <h1 style="display:flex; align-items:center; gap:10px;">
                <span class="dashicons dashicons-calculator" style="font-size:32px; width:32px; height:32px;"></span>
                Kids STEM Studio Math Assessment — Admin Control Center
            </h1>
            <p>Manage the Question Bank, customize portal accent colors, and configure exam settings easily.</p>

            <?php if (!empty($message)): ?>
                <div class="notice notice-success is-dismissible"><p><?php echo esc_html($message); ?></p></div>
            <?php endif; ?>

            <!-- ADMIN TABS NAVIGATION -->
            <h2 class="nav-tab-wrapper" style="margin-top: 20px;">
                <a href="?page=kss-math-portal&tab=questions" class="nav-tab <?php echo $active_tab === 'questions' ? 'nav-tab-active' : ''; ?>">
                    <span class="dashicons dashicons-list-view" style="vertical-align:text-top; margin-right:4px;"></span> Question Bank Manager
                </a>
                <a href="?page=kss-math-portal&tab=settings" class="nav-tab <?php echo $active_tab === 'settings' ? 'nav-tab-active' : ''; ?>">
                    <span class="dashicons dashicons-color-picker" style="vertical-align:text-top; margin-right:4px;"></span> Color Customizer & Exam Settings
                </a>
                <a href="?page=kss-math-portal&tab=progress" class="nav-tab <?php echo $active_tab === 'progress' ? 'nav-tab-active' : ''; ?>">
                    <span class="dashicons dashicons-awards" style="vertical-align:text-top; margin-right:4px;"></span> Student Progress & Mastery Reports
                </a>
            </h2>

            <?php if ($active_tab === 'questions'): ?>
                <!-- TAB 1: QUESTION BANK MANAGER -->
                <div style="display: flex; gap: 20px; margin-top: 20px; flex-wrap: wrap;">
                    <!-- LEFT COLUMN: QUESTION TABLE -->
                    <div style="flex: 2; min-width: 600px; background: #fff; border: 1px solid #ccd0d4; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                            <h2 style="margin:0;">Question Bank (<?php echo count($questions); ?> Questions)</h2>
                            <form method="post" onsubmit="return confirm('Reset Question Bank to default template?');">
                                <?php wp_nonce_field('kss_question_action', 'kss_nonce'); ?>
                                <input type="hidden" name="kss_reset_default_bank" value="1">
                                <button type="submit" class="button button-secondary">Reset to Default Bank</button>
                            </form>
                        </div>

                        <table class="wp-list-table widefat fixed striped">
                            <thead>
                                <tr>
                                    <th style="width: 50px;">ID</th>
                                    <th style="width: 60px;">Grade</th>
                                    <th style="width: 150px;">Domain</th>
                                    <th>Question Text</th>
                                    <th style="width: 110px;">Type</th>
                                    <th style="width: 120px;">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php if (empty($questions)): ?>
                                    <tr><td colspan="6">No questions found. Click "Reset to Default Bank" to pre-fill standard questions.</td></tr>
                                <?php else: ?>
                                    <?php foreach ($questions as $q): ?>
                                        <tr>
                                            <td><strong>#<?php echo esc_html($q['id']); ?></strong></td>
                                            <td><span style="background:#e0f2fe; color:#0369a1; padding:3px 8px; border-radius:12px; font-weight:bold; font-size:11px;">Grade <?php echo esc_html($q['grade']); ?></span></td>
                                            <td><?php echo esc_html($q['domain']); ?></td>
                                            <td><?php echo esc_html(mb_strimwidth($q['text'], 0, 70, '...')); ?></td>
                                            <td><em><?php echo esc_html($q['type']); ?></em></td>
                                            <td>
                                                <a href="<?php echo admin_url('admin.php?page=kss-math-portal&tab=questions&action=edit&id=' . $q['id']); ?>" class="button button-small">Edit</a>
                                                <form method="post" style="display:inline-block;" onsubmit="return confirm('Delete this question?');">
                                                    <?php wp_nonce_field('kss_question_action', 'kss_nonce'); ?>
                                                    <input type="hidden" name="kss_delete_question" value="1">
                                                    <input type="hidden" name="question_id" value="<?php echo esc_attr($q['id']); ?>">
                                                    <button type="submit" class="button button-small button-link-delete">Delete</button>
                                                </form>
                                            </td>
                                        </tr>
                                    <?php endforeach; ?>
                                <?php endif; ?>
                            </tbody>
                        </table>
                    </div>

                    <!-- RIGHT COLUMN: ADD / EDIT QUESTION FORM -->
                    <div style="flex: 1; min-width: 320px; background: #fff; border: 1px solid #ccd0d4; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); align-self: flex-start;">
                        <h2><?php echo $edit_question ? 'Edit Question #' . esc_html($edit_question['id']) : 'Add New Question'; ?></h2>
                        <form method="post">
                            <?php wp_nonce_field('kss_question_action', 'kss_nonce'); ?>
                            <input type="hidden" name="kss_save_question" value="1">
                            <input type="hidden" name="question_id" value="<?php echo esc_attr($edit_question ? $edit_question['id'] : 0); ?>">

                            <p>
                                <label><strong>Grade Level:</strong></label><br>
                                <select name="grade" style="width:100%;" required>
                                    <?php for ($g = 3; $g <= 8; $g++): ?>
                                        <option value="<?php echo $g; ?>" <?php selected($edit_question ? $edit_question['grade'] : 3, $g); ?>>Grade <?php echo $g; ?></option>
                                    <?php endfor; ?>
                                </select>
                            </p>

                            <p>
                                <label><strong>Domain / Topic:</strong></label><br>
                                <input type="text" name="domain" style="width:100%;" value="<?php echo esc_attr($edit_question ? $edit_question['domain'] : ''); ?>" required placeholder="e.g. Fractions, Ratios, Algebra">
                            </p>

                            <p>
                                <label><strong>Question Type:</strong></label><br>
                                <select name="type" id="kss_qtype" style="width:100%;" onchange="toggleQuestionTypeFields()">
                                    <option value="multiple-choice" <?php selected($edit_question ? $edit_question['type'] : 'multiple-choice', 'multiple-choice'); ?>>Multiple Choice</option>
                                    <option value="numeric-response" <?php selected($edit_question ? $edit_question['type'] : '', 'numeric-response'); ?>>Numeric Response</option>
                                </select>
                            </p>

                            <p>
                                <label><strong>Question Text:</strong></label><br>
                                <textarea name="text" style="width:100%; height:80px;" required><?php echo esc_textarea($edit_question ? $edit_question['text'] : ''); ?></textarea>
                            </p>

                            <!-- MULTIPLE CHOICE OPTIONS -->
                            <div id="mc_options_field">
                                <label><strong>Options (Check correct answer):</strong></label>
                                <?php 
                                $opts = ($edit_question && isset($edit_question['options'])) ? $edit_question['options'] : array(
                                    array('text' => '', 'correct' => true),
                                    array('text' => '', 'correct' => false),
                                    array('text' => '', 'correct' => false),
                                    array('text' => '', 'correct' => false),
                                );
                                for ($i = 0; $i < 4; $i++):
                                    $val = isset($opts[$i]['text']) ? $opts[$i]['text'] : '';
                                    $is_c = isset($opts[$i]['correct']) && $opts[$i]['correct'];
                                ?>
                                    <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                                        <input type="radio" name="correct_mc_index" value="<?php echo $i; ?>" <?php checked($is_c); ?>>
                                        <input type="text" name="options[<?php echo $i; ?>]" value="<?php echo esc_attr($val); ?>" style="flex:1;" placeholder="Option <?php echo ($i+1); ?>">
                                    </div>
                                <?php endfor; ?>
                            </div>

                            <!-- NUMERIC RESPONSE -->
                            <div id="numeric_option_field" style="display:none;">
                                <p>
                                    <label><strong>Numeric Correct Answer:</strong></label><br>
                                    <input type="text" name="correct_numeric_answer" style="width:100%;" value="<?php echo esc_attr($edit_question ? (isset($edit_question['correctAnswer']) ? $edit_question['correctAnswer'] : '') : ''); ?>" placeholder="e.g. 24 or 3.5">
                                </p>
                            </div>

                            <p>
                                <label><strong>Step-by-Step Solution Explanation:</strong></label><br>
                                <textarea name="explanation" style="width:100%; height:70px;" required placeholder="Detailed solution explanation for students..."><?php echo esc_textarea($edit_question ? $edit_question['explanation'] : ''); ?></textarea>
                            </p>

                            <p style="margin-top:15px;">
                                <button type="submit" class="button button-primary button-large" style="width:100%;">Save Question</button>
                                <?php if ($edit_question): ?>
                                    <a href="<?php echo admin_url('admin.php?page=kss-math-portal&tab=questions'); ?>" class="button button-secondary" style="width:100%; margin-top:6px; text-align:center;">Cancel Edit</a>
                                <?php endif; ?>
                            </p>
                        </form>
                    </div>
                </div>

            <?php elseif ($active_tab === 'settings'): ?>
                <!-- TAB 2: COLOR SCHEME CUSTOMIZER & EXAM SETTINGS -->
                <div style="max-w: 900px; background: #fff; border: 1px solid #ccd0d4; padding: 25px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-top: 20px;">
                    <form method="post">
                        <?php wp_nonce_field('kss_settings_action', 'kss_settings_nonce'); ?>
                        <input type="hidden" name="kss_save_settings" value="1">

                        <h2>🎨 Portal Color Scheme & Theme Customizer</h2>
                        <p class="description">Easily customize the primary accent colors, buttons, and dark header themes of the portal.</p>

                        <!-- COLOR PRESETS -->
                        <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:15px; border-radius:8px; margin-bottom:20px;">
                            <label><strong>Quick Color Presets:</strong></label><br>
                            <select id="kss_color_preset" onchange="applyColorPreset()" style="width:100%; max-w:350px; margin-top:5px;">
                                <option value="">-- Choose a Preset Theme --</option>
                                <option value="kss_classic">Kids STEM Studio Classic (Sky Blue & Teal)</option>
                                <option value="indigo_violet">Modern Indigo & Violet</option>
                                <option value="emerald_mint">Emerald & Mint Energy</option>
                                <option value="coral_sunset">Warm Sunset (Coral & Amber)</option>
                                <option value="sleek_dark">Sleek Dark Mode Accent</option>
                            </select>
                        </div>

                        <table class="form-table">
                            <tr>
                                <th scope="row"><label for="primary_color">Primary Accent Color:</label></th>
                                <td>
                                    <input type="color" name="primary_color" id="primary_color" value="<?php echo esc_attr($settings['primary_color']); ?>" style="width:50px; height:35px; vertical-align:middle; cursor:pointer;">
                                    <input type="text" id="primary_color_hex" value="<?php echo esc_attr($settings['primary_color']); ?>" onchange="syncColorInput('primary_color', this.value)" class="regular-text" style="width:100px; font-weight:bold;">
                                    <p class="description">Main highlight color used for active timeline steps, links, and headers (Default: #4DA8FF).</p>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"><label for="secondary_color">Secondary Accent Color:</label></th>
                                <td>
                                    <input type="color" name="secondary_color" id="secondary_color" value="<?php echo esc_attr($settings['secondary_color']); ?>" style="width:50px; height:35px; vertical-align:middle; cursor:pointer;">
                                    <input type="text" id="secondary_color_hex" value="<?php echo esc_attr($settings['secondary_color']); ?>" onchange="syncColorInput('secondary_color', this.value)" class="regular-text" style="width:100px; font-weight:bold;">
                                    <p class="description">Used for success metrics, recommendations, and badges (Default: #5ECF7A).</p>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"><label for="brand_teal_color">Brand Button Gradient Color:</label></th>
                                <td>
                                    <input type="color" name="brand_teal_color" id="brand_teal_color" value="<?php echo esc_attr($settings['brand_teal_color']); ?>" style="width:50px; height:35px; vertical-align:middle; cursor:pointer;">
                                    <input type="text" id="brand_teal_color_hex" value="<?php echo esc_attr($settings['brand_teal_color']); ?>" onchange="syncColorInput('brand_teal_color', this.value)" class="regular-text" style="width:100px; font-weight:bold;">
                                    <p class="description">Main action button color (Default: #2fbdb9).</p>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"><label for="navy_dark_color">Header & Dark Background Color:</label></th>
                                <td>
                                    <input type="color" name="navy_dark_color" id="navy_dark_color" value="<?php echo esc_attr($settings['navy_dark_color']); ?>" style="width:50px; height:35px; vertical-align:middle; cursor:pointer;">
                                    <input type="text" id="navy_dark_color_hex" value="<?php echo esc_attr($settings['navy_dark_color']); ?>" onchange="syncColorInput('navy_dark_color', this.value)" class="regular-text" style="width:100px; font-weight:bold;">
                                    <p class="description">Used for main typography, login background, and footer (Default: #263238).</p>
                                </td>
                            </tr>
                        </table>

                        <hr style="margin:25px 0;">

                        <h2>⚙️ Assessment Rules & Track Toggles</h2>
                        <table class="form-table">
                            <tr>
                                <th scope="row"><label for="questions_per_exam">Questions Per Exam:</label></th>
                                <td>
                                    <input type="number" name="questions_per_exam" id="questions_per_exam" value="<?php echo esc_attr($settings['questions_per_exam']); ?>" min="5" max="50" style="width:100px;">
                                    <p class="description">Number of questions served during each assessment (Default: 15).</p>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Countdown / Elapsed Timer:</th>
                                <td>
                                    <label><input type="checkbox" name="enable_timer" value="1" <?php checked($settings['enable_timer']); ?>> Display Live Timer during exam</label>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Enabled Test Tracks:</th>
                                <td>
                                    <label style="margin-right:15px;"><input type="checkbox" name="enable_track_3_4" value="1" <?php checked($settings['enable_track_3_4']); ?>> Grades 3–4 Track</label>
                                    <label style="margin-right:15px;"><input type="checkbox" name="enable_track_5_6" value="1" <?php checked($settings['enable_track_5_6']); ?>> Grades 5–6 Track</label>
                                    <label><input type="checkbox" name="enable_track_7_8" value="1" <?php checked($settings['enable_track_7_8']); ?>> Grades 7–8 Track</label>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Instant Results & Solutions:</th>
                                <td>
                                    <label><input type="checkbox" name="show_instant_results" value="1" <?php checked($settings['show_instant_results']); ?>> Show score and step-by-step breakdown immediately after exam</label>
                                </td>
                            </tr>
                        </table>

                        <p class="submit" style="margin-top:20px;">
                            <button type="submit" class="button button-primary button-large">Save All Colors & Settings</button>
                        </p>
                    </form>
                </div>

            <?php elseif ($active_tab === 'progress'): ?>
                <!-- TAB 3: STUDENT PROGRESS & MASTERY REPORTS -->
                <div style="background: #fff; border: 1px solid #ccd0d4; padding: 25px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-top: 20px;">
                    <h2>🏆 Student Progress & Digital Worksheet Mastery Reports</h2>
                    <p class="description">Review persistent student learning progress, placement exam diagnoses, unlocked lesson levels, completed worksheets, and stars earned.</p>

                    <?php
                    $progress_records = get_option('kss_math_student_progress_records', array());
                    $saved_attempts = get_option('kss_math_saved_attempts', array());
                    ?>

                    <table class="wp-list-table widefat fixed striped" style="margin-top: 20px;">
                        <thead>
                            <tr>
                                <th style="width: 160px;">Student Name</th>
                                <th style="width: 110px;">Placed Grade</th>
                                <th style="width: 140px;">Highest Unlocked</th>
                                <th style="width: 130px;">Worksheets Solved</th>
                                <th style="width: 110px;">Stars Earned</th>
                                <th style="width: 110px;">Max Streak</th>
                                <th>Last Active Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php if (empty($progress_records) && empty($saved_attempts)): ?>
                                <tr>
                                    <td colspan="7" style="text-align:center; padding: 25px; color:#64748b;">
                                        No student progress records recorded yet. Once students take placement exams or complete worksheets, their real-time diagnostics will appear here.
                                    </td>
                                </tr>
                            <?php else: ?>
                                <?php 
                                // Merge and display progress records
                                foreach ($progress_records as $rec): 
                                    $uname = esc_html($rec['user_name'] ?? 'Student');
                                    $p = $rec['progress'] ?? array();
                                    $placed = esc_html($p['testedGrade'] ? 'Grade ' . $p['testedGrade'] : 'In Progress');
                                    $unlocked = isset($p['unlockedLessonIndex']) ? 'G' . ($p['testedGrade'] ?? 3) . ' L' . ($p['unlockedLessonIndex'][strval($p['testedGrade'] ?? 3)] ?? 1) : 'G3 L1';
                                    $completedCount = isset($p['completedLessons']) ? count($p['completedLessons']) : 0;
                                    $stars = intval($p['totalStars'] ?? 0);
                                    $streak = intval($p['highestStreak'] ?? 0);
                                    $date = esc_html(isset($rec['updated_at']) ? date('M j, Y g:ia', strtotime($rec['updated_at'])) : 'Recent');
                                ?>
                                <tr>
                                    <td><strong><?php echo $uname; ?></strong></td>
                                    <td><span class="dashicons dashicons-yes-alt" style="color:#059669;"></span> <?php echo $placed; ?></td>
                                    <td><code><?php echo esc_html($unlocked); ?></code></td>
                                    <td><?php echo $completedCount; ?> Worksheets</td>
                                    <td><span style="color:#f59e0b; font-weight:bold;">⭐ <?php echo $stars; ?></span></td>
                                    <td><span style="color:#ea580c; font-weight:bold;">🔥 <?php echo $streak; ?></span></td>
                                    <td><?php echo $date; ?></td>
                                </tr>
                                <?php endforeach; ?>
                            <?php endif; ?>
                        </tbody>
                    </table>
                </div>

            <?php endif; ?>
        </div>

        <script>
            function toggleQuestionTypeFields() {
                var qtype = document.getElementById('kss_qtype');
                if (!qtype) return;
                if (qtype.value === 'numeric-response') {
                    document.getElementById('mc_options_field').style.display = 'none';
                    document.getElementById('numeric_option_field').style.display = 'block';
                } else {
                    document.getElementById('mc_options_field').style.display = 'block';
                    document.getElementById('numeric_option_field').style.display = 'none';
                }
            }
            toggleQuestionTypeFields();

            function syncColorInput(id, hex) {
                var picker = document.getElementById(id);
                if (picker) picker.value = hex;
            }

            function applyColorPreset() {
                var val = document.getElementById('kss_color_preset').value;
                var presets = {
                    'kss_classic': { primary: '#4DA8FF', secondary: '#5ECF7A', brand: '#2fbdb9', dark: '#263238' },
                    'indigo_violet': { primary: '#6366f1', secondary: '#10b981', brand: '#4f46e5', dark: '#1e1b4b' },
                    'emerald_mint': { primary: '#059669', secondary: '#34d399', brand: '#047857', dark: '#064e3b' },
                    'coral_sunset': { primary: '#f97316', secondary: '#fbbf24', brand: '#ea580c', dark: '#431407' },
                    'sleek_dark': { primary: '#38bdf8', secondary: '#4ade80', brand: '#0284c7', dark: '#0f172a' }
                };

                if (presets[val]) {
                    var p = presets[val];
                    document.getElementById('primary_color').value = p.primary;
                    document.getElementById('primary_color_hex').value = p.primary;
                    document.getElementById('secondary_color').value = p.secondary;
                    document.getElementById('secondary_color_hex').value = p.secondary;
                    document.getElementById('brand_teal_color').value = p.brand;
                    document.getElementById('brand_teal_color_hex').value = p.brand;
                    document.getElementById('navy_dark_color').value = p.dark;
                    document.getElementById('navy_dark_color_hex').value = p.dark;
                }
            }

            document.querySelectorAll('input[type="color"]').forEach(function(picker) {
                picker.addEventListener('input', function() {
                    var hexInput = document.getElementById(this.id + '_hex');
                    if (hexInput) hexInput.value = this.value;
                });
            });
        </script>
        <?php
    }

    private function handle_save_question($data) {
        $raw = get_option('kss_math_question_bank', '[]');
        $questions = json_decode($raw, true) ?: array();

        $id = intval($data['question_id']);
        $grade = intval($data['grade']);
        $domain = sanitize_text_field($data['domain']);
        $text = sanitize_textarea_field($data['text']);
        $type = sanitize_text_field($data['type']);
        $explanation = sanitize_textarea_field($data['explanation']);

        $question_obj = array(
            'id' => ($id > 0) ? $id : (count($questions) > 0 ? max(array_column($questions, 'id')) + 1 : 101),
            'grade' => $grade,
            'domain' => $domain,
            'text' => $text,
            'type' => $type,
            'explanation' => $explanation
        );

        if ($type === 'multiple-choice') {
            $opts = array();
            $correct_idx = isset($data['correct_mc_index']) ? intval($data['correct_mc_index']) : 0;
            if (isset($data['options']) && is_array($data['options'])) {
                foreach ($data['options'] as $idx => $opt_text) {
                    $opts[] = array(
                        'text' => sanitize_text_field($opt_text),
                        'correct' => ($idx === $correct_idx)
                    );
                }
            }
            $question_obj['options'] = $opts;
        } else {
            $question_obj['correctAnswer'] = sanitize_text_field($data['correct_numeric_answer']);
        }

        if ($id > 0) {
            foreach ($questions as $index => $q) {
                if ($q['id'] === $id) {
                    $questions[$index] = $question_obj;
                    break;
                }
            }
        } else {
            $questions[] = $question_obj;
        }

        update_option('kss_math_question_bank', json_encode($questions));
    }

    private function handle_delete_question($id) {
        $raw = get_option('kss_math_question_bank', '[]');
        $questions = json_decode($raw, true) ?: array();
        $filtered = array_values(array_filter($questions, function($q) use ($id) {
            return $q['id'] !== $id;
        }));
        update_option('kss_math_question_bank', json_encode($filtered));
    }

    private function handle_save_settings($data) {
        $settings = array(
            'primary_color' => sanitize_hex_color($data['primary_color']) ?: '#4DA8FF',
            'secondary_color' => sanitize_hex_color($data['secondary_color']) ?: '#5ECF7A',
            'brand_teal_color' => sanitize_hex_color($data['brand_teal_color']) ?: '#2fbdb9',
            'navy_dark_color' => sanitize_hex_color($data['navy_dark_color']) ?: '#263238',
            'questions_per_exam' => intval($data['questions_per_exam']),
            'enable_timer' => isset($data['enable_timer']),
            'enable_track_3_4' => isset($data['enable_track_3_4']),
            'enable_track_5_6' => isset($data['enable_track_5_6']),
            'enable_track_7_8' => isset($data['enable_track_7_8']),
            'show_instant_results' => isset($data['show_instant_results'])
        );
        update_option('kss_math_portal_settings', json_encode($settings));
    }

    public function register_rest_routes() {
        register_rest_route('kss-math/v1', '/questions', array(
            'methods' => 'GET',
            'callback' => array($this, 'rest_get_questions'),
            'permission_callback' => '__return_true'
        ));

        register_rest_route('kss-math/v1', '/settings', array(
            'methods' => 'GET',
            'callback' => array($this, 'rest_get_settings'),
            'permission_callback' => '__return_true'
        ));

        register_rest_route('kss-math/v1', '/save-attempt', array(
            'methods' => 'POST',
            'callback' => array($this, 'rest_save_attempt'),
            'permission_callback' => '__return_true'
        ));

        register_rest_route('kss-math/v1', '/student-progress', array(
            'methods' => 'POST',
            'callback' => array($this, 'rest_save_student_progress'),
            'permission_callback' => '__return_true'
        ));

        register_rest_route('kss-math/v1', '/student-progress', array(
            'methods' => 'GET',
            'callback' => array($this, 'rest_get_student_progress'),
            'permission_callback' => '__return_true'
        ));
    }

    public function rest_get_questions() {
        $raw = get_option('kss_math_question_bank', '[]');
        $questions = json_decode($raw, true) ?: array();
        return rest_ensure_response($questions);
    }

    public function rest_get_settings() {
        $raw = get_option('kss_math_portal_settings', '[]');
        $settings = array_merge($this->get_default_settings(), json_decode($raw, true) ?: array());
        return rest_ensure_response($settings);
    }

    public function rest_save_attempt($request) {
        $params = $request->get_json_params();
        if (empty($params)) {
            return new WP_Error('invalid_data', 'No data provided', array('status' => 400));
        }

        $attempts = get_option('kss_math_saved_attempts', array());
        $attempts[] = $params;
        update_option('kss_math_saved_attempts', $attempts);

        $user_id = intval($params['user_id'] ?? 0);
        if ($user_id > 0) {
            $existing_meta = get_user_meta($user_id, 'kss_math_attempts', true) ?: array();
            $existing_meta[] = $params;
            update_user_meta($user_id, 'kss_math_attempts', $existing_meta);
            if (!empty($params['recommendedGrade'])) {
                update_user_meta($user_id, 'kss_math_placed_grade', sanitize_text_field($params['recommendedGrade']));
            }
        }

        return rest_ensure_response(array('success' => true, 'message' => 'Attempt saved successfully'));
    }

    public function rest_save_student_progress($request) {
        $params = $request->get_json_params();
        if (empty($params)) {
            return new WP_Error('invalid_data', 'No data provided', array('status' => 400));
        }

        $user_id = intval($params['user_id'] ?? 0);
        $progress = $params['progress'] ?? array();
        $user_name = sanitize_text_field($params['user_name'] ?? 'Student');

        // Persist to user meta if user is registered
        if ($user_id > 0) {
            update_user_meta($user_id, 'kss_math_progress', $progress);
        }

        // Update centralized records option for teacher/admin dashboard
        $records = get_option('kss_math_student_progress_records', array());
        $record_key = ($user_id > 0) ? 'user_' . $user_id : 'guest_' . substr(md5($user_name), 0, 8);
        $records[$record_key] = array(
            'user_id' => $user_id,
            'user_name' => $user_name,
            'progress' => $progress,
            'updated_at' => current_time('mysql')
        );
        update_option('kss_math_student_progress_records', $records);

        return rest_ensure_response(array('success' => true, 'message' => 'Student progress synchronized successfully'));
    }

    public function rest_get_student_progress($request) {
        $user_id = intval($request->get_param('user_id') ?: get_current_user_id());
        if ($user_id <= 0) {
            return new WP_Error('invalid_user', 'Valid student user ID required', array('status' => 400));
        }

        $progress = get_user_meta($user_id, 'kss_math_progress', true);
        return rest_ensure_response(array('success' => true, 'progress' => $progress ?: null));
    }

    // SHORTCODE RENDERS FOR ELEMENTOR
    public function render_login_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/login.html" style="width:100%; height:800px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_portal_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/portal.html" style="width:100%; height:900px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_instructions_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/instructions.html" style="width:100%; height:750px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_exam_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/exam.html" style="width:100%; height:950px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_results_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/results.html" style="width:100%; height:1100px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_practice_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/practice.html" style="width:100%; height:950px; border:none; border-radius:16px;"></iframe></div>';
    }

    private function get_default_settings() {
        return array(
            'primary_color' => '#4DA8FF',
            'secondary_color' => '#5ECF7A',
            'brand_teal_color' => '#2fbdb9',
            'navy_dark_color' => '#263238',
            'questions_per_exam' => 15,
            'enable_timer' => true,
            'enable_track_3_4' => true,
            'enable_track_5_6' => true,
            'enable_track_7_8' => true,
            'show_instant_results' => true
        );
    }

    private function get_default_question_bank() {
        return array(
            array(
                "id" => 101, "grade" => 3, "domain" => "Multiplication Concepts",
                "text" => "A bakery boxes donuts in groups of 6. If a customer buys 4 boxes, how many donuts do they get in total?",
                "type" => "multiple-choice",
                "options" => array(
                    array("text" => "24", "correct" => true),
                    array("text" => "10", "correct" => false),
                    array("text" => "18", "correct" => false),
                    array("text" => "12", "correct" => false)
                ),
                "explanation" => "Multiply the number of boxes by the number of donuts per box: 4 x 6 = 24."
            ),
            array(
                "id" => 102, "grade" => 3, "domain" => "Multiplication Properties",
                "text" => "Which equation shows the Commutative Property of Multiplication?",
                "type" => "multiple-choice",
                "options" => array(
                    array("text" => "4 x 5 = 5 x 4", "correct" => true),
                    array("text" => "4 x 5 = 20", "correct" => false),
                    array("text" => "(4 x 2) x 5 = 4 x (2 x 5)", "correct" => false),
                    array("text" => "4 x 0 = 0", "correct" => false)
                ),
                "explanation" => "The Commutative Property states that changing the order of factors does not change the product: a x b = b x a."
            ),
            array(
                "id" => 103, "grade" => 3, "domain" => "Division Concepts",
                "text" => "If 32 books are shared equally among 4 shelves, how many books go on each shelf?",
                "type" => "numeric-response",
                "correctAnswer" => "8",
                "explanation" => "Divide the total books by the number of shelves: 32 / 4 = 8 books per shelf."
            )
        );
    }
}

new KSS_Math_Portal_Plugin();
