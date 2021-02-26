;;
;; Setup cmake3-mode for autoloading
;;
(autoload 'cmake3-mode "cmake3-mode" "Major mode for editing CMake listfiles." t)
(setq auto-mode-alist
          (append
           '(("CMakeLists\\.txt\\'" . cmake3-mode))
           '(("\\.cmake\\'" . cmake3-mode))
           auto-mode-alist))
