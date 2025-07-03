document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const counter = document.querySelector('.slider-counter');
    const thumbs = document.querySelectorAll('.thumb');
    const playPauseBtn = document.querySelector('.play-pause-btn');
    
    let currentSlide = 0;
    const totalSlides = slides.length;
    let autoPlayInterval;
    let isPlaying = true;
    
    // Инициализация миниатюр
    initThumbnails();
    
    // Начало автопрокрутки
    startAutoPlay();
    
    // Показать первый слайд
    showSlide(currentSlide);
    
    // Обработчики кнопок
    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);
    
    // Кнопка play/pause
    playPauseBtn.addEventListener('click', togglePlayPause);
    
    // Обработчики клавиатуры
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowRight') nextSlide();
        if (e.key === 'ArrowLeft') prevSlide();
        if (e.key === ' ') togglePlayPause();
    });
    
    // Инициализация миниатюр
    function initThumbnails() {
        slides.forEach((slide, index) => {
            thumbs[index].style.backgroundImage = `url(${slide.src})`;
            thumbs[index].addEventListener('click', () => showSlide(index));
        });
    }
    
    // Функции навигации
    function nextSlide() {
        showSlide((currentSlide + 1) % totalSlides);
    }
    
    function prevSlide() {
        showSlide((currentSlide - 1 + totalSlides) % totalSlides);
    }
    
    // Показать слайд
    function showSlide(index) {
        slides[currentSlide].classList.remove('active');
        thumbs[currentSlide].classList.remove('active');
        
        currentSlide = index;
        
        slides[currentSlide].classList.add('active');
        thumbs[currentSlide].classList.add('active');
        updateCounter();
    }
    
    // Обновление счетчика
    function updateCounter() {
        counter.textContent = `Изображение ${currentSlide + 1} из ${totalSlides}`;
    }
    
    
    // Автопрокрутка
    function startAutoPlay() {
        if (autoPlayInterval) clearInterval(autoPlayInterval);
        autoPlayInterval = setInterval(nextSlide, 3000);
        isPlaying = true;
        playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
    }
    
    function stopAutoPlay() {
        clearInterval(autoPlayInterval);
        isPlaying = false;
        playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
    }
    
    function togglePlayPause() {
        if (isPlaying) {
            stopAutoPlay();
        } else {
            startAutoPlay();
        }
    }
    
    // Пауза при наведении
    sliderWrapper = document.querySelector('.slider-wrapper');
    sliderWrapper.addEventListener('mouseenter', stopAutoPlay);
    sliderWrapper.addEventListener('mouseleave', () => {
        if (isPlaying) startAutoPlay();
    });
});