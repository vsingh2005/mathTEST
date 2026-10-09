<?php
/**
 * Theme functions and definitions
 *
 * @package HelloElementor
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // Exit if accessed directly.
}

define( 'HELLO_ELEMENTOR_VERSION', '3.4.9' );
define( 'EHP_THEME_SLUG', 'hello-elementor' );

define( 'HELLO_THEME_PATH', get_template_directory() );
define( 'HELLO_THEME_URL', get_template_directory_uri() );
define( 'HELLO_THEME_ASSETS_PATH', HELLO_THEME_PATH . '/assets/' );
define( 'HELLO_THEME_ASSETS_URL', HELLO_THEME_URL . '/assets/' );
define( 'HELLO_THEME_SCRIPTS_PATH', HELLO_THEME_ASSETS_PATH . 'js/' );
define( 'HELLO_THEME_SCRIPTS_URL', HELLO_THEME_ASSETS_URL . 'js/' );
define( 'HELLO_THEME_STYLE_PATH', HELLO_THEME_ASSETS_PATH . 'css/' );
define( 'HELLO_THEME_STYLE_URL', HELLO_THEME_ASSETS_URL . 'css/' );
define( 'HELLO_THEME_IMAGES_PATH', HELLO_THEME_ASSETS_PATH . 'images/' );
define( 'HELLO_THEME_IMAGES_URL', HELLO_THEME_ASSETS_URL . 'images/' );

if ( ! isset( $content_width ) ) {
	$content_width = 800; // Pixels.
}

if ( ! function_exists( 'hello_elementor_setup' ) ) {
	/**
	 * Set up theme support.
	 *
	 * @return void
	 */
	function hello_elementor_setup() {
		if ( is_admin() ) {
			hello_maybe_update_theme_version_in_db();
		}

		if ( apply_filters( 'hello_elementor_register_menus', true ) ) {
			register_nav_menus( [ 'menu-1' => esc_html__( 'Header', 'hello-elementor' ) ] );
			register_nav_menus( [ 'menu-2' => esc_html__( 'Footer', 'hello-elementor' ) ] );
		}

		if ( apply_filters( 'hello_elementor_post_type_support', true ) ) {
			add_post_type_support( 'page', 'excerpt' );
		}

		if ( apply_filters( 'hello_elementor_add_theme_support', true ) ) {
			add_theme_support( 'post-thumbnails' );
			add_theme_support( 'automatic-feed-links' );
			add_theme_support( 'title-tag' );
			add_theme_support(
				'html5',
				[
					'search-form',
					'comment-form',
					'comment-list',
					'gallery',
					'caption',
					'script',
					'style',
					'navigation-widgets',
				]
			);
			add_theme_support(
				'custom-logo',
				[
					'height'      => 100,
					'width'       => 350,
					'flex-height' => true,
					'flex-width'  => true,
				]
			);
			add_theme_support( 'align-wide' );
			add_theme_support( 'responsive-embeds' );

			/*
			 * Editor Styles
			 */
			add_theme_support( 'editor-styles' );
			add_editor_style( 'assets/css/editor-styles.css' );

			/*
			 * WooCommerce.
			 */
			if ( apply_filters( 'hello_elementor_add_woocommerce_support', true ) ) {
				// WooCommerce in general.
				add_theme_support( 'woocommerce' );
				// Enabling WooCommerce product gallery features (are off by default since WC 3.0.0).
				// zoom.
				add_theme_support( 'wc-product-gallery-zoom' );
				// lightbox.
				add_theme_support( 'wc-product-gallery-lightbox' );
				// swipe.
				add_theme_support( 'wc-product-gallery-slider' );
			}
		}
	}
}
add_action( 'after_setup_theme', 'hello_elementor_setup' );

function hello_maybe_update_theme_version_in_db() {
	$theme_version_option_name = 'hello_theme_version';
	// The theme version saved in the database.
	$hello_theme_db_version = get_option( $theme_version_option_name );

	// If the 'hello_theme_version' option does not exist in the DB, or the version needs to be updated, do the update.
	if ( ! $hello_theme_db_version || version_compare( $hello_theme_db_version, HELLO_ELEMENTOR_VERSION, '<' ) ) {
		update_option( $theme_version_option_name, HELLO_ELEMENTOR_VERSION );
	}
}

if ( ! function_exists( 'hello_elementor_display_header_footer' ) ) {
	/**
	 * Check whether to display header footer.
	 *
	 * @return bool
	 */
	function hello_elementor_display_header_footer() {
		$hello_elementor_header_footer = true;

		return apply_filters( 'hello_elementor_header_footer', $hello_elementor_header_footer );
	}
}

if ( ! function_exists( 'hello_elementor_scripts_styles' ) ) {
	/**
	 * Theme Scripts & Styles.
	 *
	 * @return void
	 */
	function hello_elementor_scripts_styles() {
		if ( apply_filters( 'hello_elementor_enqueue_style', true ) ) {
			wp_enqueue_style(
				'hello-elementor',
				HELLO_THEME_STYLE_URL . 'reset.css',
				[],
				HELLO_ELEMENTOR_VERSION
			);
		}

		if ( apply_filters( 'hello_elementor_enqueue_theme_style', true ) ) {
			wp_enqueue_style(
				'hello-elementor-theme-style',
				HELLO_THEME_STYLE_URL . 'theme.css',
				[],
				HELLO_ELEMENTOR_VERSION
			);
		}

		if ( hello_elementor_display_header_footer() ) {
			wp_enqueue_style(
				'hello-elementor-header-footer',
				HELLO_THEME_STYLE_URL . 'header-footer.css',
				[],
				HELLO_ELEMENTOR_VERSION
			);
		}
	}
}
add_action( 'wp_enqueue_scripts', 'hello_elementor_scripts_styles' );

if ( ! function_exists( 'hello_elementor_register_elementor_locations' ) ) {
	/**
	 * Register Elementor Locations.
	 *
	 * @param ElementorPro\Modules\ThemeBuilder\Classes\Locations_Manager $elementor_theme_manager theme manager.
	 *
	 * @return void
	 */
	function hello_elementor_register_elementor_locations( $elementor_theme_manager ) {
		if ( apply_filters( 'hello_elementor_register_elementor_locations', true ) ) {
			$elementor_theme_manager->register_all_core_location();
		}
	}
}
add_action( 'elementor/theme/register_locations', 'hello_elementor_register_elementor_locations' );

if ( ! function_exists( 'hello_elementor_content_width' ) ) {
	/**
	 * Set default content width.
	 *
	 * @return void
	 */
	function hello_elementor_content_width() {
		$GLOBALS['content_width'] = apply_filters( 'hello_elementor_content_width', 800 );
	}
}
add_action( 'after_setup_theme', 'hello_elementor_content_width', 0 );

if ( ! function_exists( 'hello_elementor_add_description_meta_tag' ) ) {
	/**
	 * Add description meta tag with excerpt text.
	 *
	 * @return void
	 */
	function hello_elementor_add_description_meta_tag() {
		if ( ! apply_filters( 'hello_elementor_description_meta_tag', true ) ) {
			return;
		}

		if ( ! is_singular() ) {
			return;
		}

		$post = get_queried_object();
		if ( empty( $post->post_excerpt ) ) {
			return;
		}

		echo '<meta name="description" content="' . esc_attr( wp_strip_all_tags( $post->post_excerpt ) ) . '">' . "\n";
	}
}
add_action( 'wp_head', 'hello_elementor_add_description_meta_tag' );

// Settings page
require get_template_directory() . '/includes/settings-functions.php';

// Header & footer styling option, inside Elementor
require get_template_directory() . '/includes/elementor-functions.php';

if ( ! function_exists( 'hello_elementor_customizer' ) ) {
	// Customizer controls
	function hello_elementor_customizer() {
		if ( ! is_customize_preview() ) {
			return;
		}

		if ( ! hello_elementor_display_header_footer() ) {
			return;
		}

		require get_template_directory() . '/includes/customizer-functions.php';
	}
}
add_action( 'init', 'hello_elementor_customizer' );

if ( ! function_exists( 'hello_elementor_check_hide_title' ) ) {
	/**
	 * Check whether to display the page title.
	 *
	 * @param bool $val default value.
	 *
	 * @return bool
	 */
	function hello_elementor_check_hide_title( $val ) {
		if ( defined( 'ELEMENTOR_VERSION' ) ) {
			$current_doc = Elementor\Plugin::instance()->documents->get( get_the_ID() );
			if ( $current_doc && 'yes' === $current_doc->get_settings( 'hide_title' ) ) {
				$val = false;
			}
		}
		return $val;
	}
}
add_filter( 'hello_elementor_page_title', 'hello_elementor_check_hide_title' );

/**
 * BC:
 * In v2.7.0 the theme removed the `hello_elementor_body_open()` from `header.php` replacing it with `wp_body_open()`.
 * The following code prevents fatal errors in child themes that still use this function.
 */
if ( ! function_exists( 'hello_elementor_body_open' ) ) {
	function hello_elementor_body_open() {
		wp_body_open();
	}
}

require HELLO_THEME_PATH . '/theme.php';

HelloTheme\Theme::instance();

// 1. REGISTER THE PLACEMENT TEST API ENDPOINT
add_action('rest_api_init', function () {
    register_rest_route('kss-math/v1', '/save-attempt', array(
        'methods'             => 'POST',
        'callback'            => 'kss_save_math_attempt',
        'permission_callback' => 'is_user_logged_in', // Restricts to logged-in sessions/JWT
    ));

    register_rest_route('kss-math/v1', '/get-attempts', array(
        'methods'             => 'GET',
        'callback'            => 'kss_get_math_attempts',
        'permission_callback' => 'is_user_logged_in', // Restricts to logged-in sessions/JWT
    ));

    register_rest_route('kss-math/v1', '/student-progress', array(
        'methods'             => 'POST',
        'callback'            => 'kss_save_student_progress_theme',
        'permission_callback' => '__return_true',
    ));

    register_rest_route('kss-math/v1', '/student-progress', array(
        'methods'             => 'GET',
        'callback'            => 'kss_get_student_progress_theme',
        'permission_callback' => '__return_true',
    ));
});

function kss_get_math_attempts(WP_REST_Request $request) {
    $user_id = get_current_user_id();
    if (!$user_id) {
        return new WP_Error('no_user', 'Unauthorized access', array('status' => 401));
    }

    $attempts = get_user_meta($user_id, 'kss_math_attempts', true);
    if (!is_array($attempts)) {
        $attempts = array();
    }

    return new WP_REST_Response(array('success' => true, 'attempts' => $attempts), 200);
}

function kss_save_math_attempt(WP_REST_Request $request) {
    $user_id = get_current_user_id();
    if (!$user_id) {
        return new WP_Error('no_user', 'Unauthorized access', array('status' => 401));
    }

    $params = $request->get_json_params();
    $score = sanitize_text_field($params['score']);
    $recommended_level = sanitize_text_field($params['recommendedLevel']);
    $time_elapsed = intval($params['timeElapsedSeconds']);
    $answers = $params['answers']; 

    $attempts = get_user_meta($user_id, 'kss_math_attempts', true);
    if (!is_array($attempts)) {
        $attempts = array();
    }

    $new_attempt = array(
        'timestamp'          => current_time('mysql'),
        'score'              => $score,
        'recommendedLevel'   => $recommended_level,
        'timeElapsedSeconds' => $time_elapsed,
        'answers'            => $answers
    );
    $attempts[] = $new_attempt;

    update_user_meta($user_id, 'kss_math_attempts', $attempts);
    return new WP_REST_Response(array('success' => true, 'attempt' => $new_attempt), 200);
}

function kss_save_student_progress_theme(WP_REST_Request $request) {
    $params = $request->get_json_params();
    if (empty($params)) {
        return new WP_Error('invalid_data', 'No data provided', array('status' => 400));
    }

    $user_id = intval($params['user_id'] ?? get_current_user_id());
    $progress = $params['progress'] ?? array();
    $user_name = sanitize_text_field($params['user_name'] ?? 'Student');

    if ($user_id > 0) {
        update_user_meta($user_id, 'kss_math_progress', $progress);
    }

    $records = get_option('kss_math_student_progress_records', array());
    $record_key = ($user_id > 0) ? 'user_' . $user_id : 'guest_' . substr(md5($user_name), 0, 8);
    $records[$record_key] = array(
        'user_id' => $user_id,
        'user_name' => $user_name,
        'progress' => $progress,
        'updated_at' => current_time('mysql')
    );
    update_option('kss_math_student_progress_records', $records);

    return new WP_REST_Response(array('success' => true, 'message' => 'Progress saved successfully'), 200);
}

function kss_get_student_progress_theme(WP_REST_Request $request) {
    $user_id = intval($request->get_param('user_id') ?: get_current_user_id());
    if ($user_id <= 0) {
        return new WP_Error('invalid_user', 'Valid student user ID required', array('status' => 400));
    }

    $progress = get_user_meta($user_id, 'kss_math_progress', true);
    return new WP_REST_Response(array('success' => true, 'progress' => $progress ?: null), 200);
}

// 2. DISPLAY LOGS ON THE USER PROFILE SCREEN IN THE ADMIN PANEL
add_action('show_user_profile', 'kss_display_math_attempts');
add_action('edit_user_profile', 'kss_display_math_attempts');

function kss_display_math_attempts($user) {
    $attempts = get_user_meta($user->ID, 'kss_math_attempts', true);
    ?>
    <h2>Math Placement Test Logs</h2>
    <table class="form-table">
        <tr>
            <th>Placement History</th>
            <td>
                <?php if (empty($attempts)) : ?>
                    <p>No placement test attempts found for this user.</p>
                <?php else : ?>
                    <table class="wp-list-table widefat fixed striped" style="max-width: 800px;">
                        <thead>
                            <tr>
                                <th style="font-weight: bold; width: 180px;">Date & Time</th>
                                <th style="font-weight: bold; width: 100px;">Score</th>
                                <th style="font-weight: bold; width: 200px;">Recommended Level</th>
                                <th style="font-weight: bold;">Time Taken</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($attempts as $attempt) : ?>
                                <tr>
                                    <td><?php echo esc_html($attempt['timestamp']); ?></td>
                                    <td><?php echo esc_html($attempt['score']); ?></td>
                                    <td><?php echo esc_html($attempt['recommendedLevel']); ?></td>
                                    <td><?php echo esc_html(floor($attempt['timeElapsedSeconds'] / 60)); ?>m <?php echo esc_html($attempt['timeElapsedSeconds'] % 60); ?>s</td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                <?php endif; ?>
            </td>
        </tr>
    </table>
    <?php
}

